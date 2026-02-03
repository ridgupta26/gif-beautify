from flask import Flask, render_template, request, send_file, jsonify
import os
from werkzeug.utils import secure_filename
import tempfile
from gif_processor import process_gif
import time
import requests
from io import BytesIO
import zipfile
import json

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

ALLOWED_EXTENSIONS = {'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Only GIF files are allowed'}), 400
        
        # Get settings from form
        target_size = float(request.form.get('targetSize', 5.0))
        gif_width = int(request.form.get('gifWidth', 1900))
        border_radius = int(request.form.get('borderRadius', 0))
        shadow_size = request.form.get('shadowSize', 'medium')
        background_type = request.form.get('backgroundType', 'gradient')
        gradient_start = request.form.get('gradientStart', '#ffffff')
        gradient_end = request.form.get('gradientEnd', '#ffffff')
        background_image_url = request.form.get('backgroundImageUrl', '')
        offset_x = int(request.form.get('offsetX', 0))
        offset_y = int(request.form.get('offsetY', 0))
        add_background = request.form.get('addBackground', 'false') == 'true'
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        timestamp = str(int(time.time()))
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{timestamp}_{filename}")
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{timestamp}_compressed_{filename}")
        
        file.save(input_path)
        
        # Get original file size
        original_size = os.path.getsize(input_path)
        
        # Handle background image - either local static file or external URL
        background_image_path = None
        if background_type == 'image' and background_image_url and add_background:
            # Check if it's a local static file (starts with /static/)
            if background_image_url.startswith('/static/'):
                # It's a local file - construct the path
                local_filename = background_image_url.replace('/static/', '')
                static_file_path = os.path.join(os.path.dirname(__file__), 'static', local_filename)
                
                if os.path.exists(static_file_path):
                    # Copy to temp directory so we can use it
                    background_image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{timestamp}_bg.jpg")
                    import shutil
                    shutil.copy2(static_file_path, background_image_path)
                    print(f"Using local wallpaper: {local_filename}")
                else:
                    print(f"Local wallpaper not found: {static_file_path}")
                    background_type = 'gradient'
            else:
                # It's an external URL - download it
                try:
                    response = requests.get(background_image_url, timeout=10)
                    if response.status_code == 200:
                        background_image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{timestamp}_bg.jpg")
                        with open(background_image_path, 'wb') as f:
                            f.write(response.content)
                        print(f"Downloaded external wallpaper: {background_image_url}")
                except Exception as e:
                    print(f"Failed to download background image: {e}")
                    # Fall back to gradient
                    background_type = 'gradient'
        
        # Process the GIF
        result = process_gif(
            input_path=input_path,
            output_path=output_path,
            target_size_mb=target_size,
            target_width=gif_width,
            border_radius=border_radius,
            shadow_size=shadow_size,
            gradient_start=gradient_start,
            gradient_end=gradient_end,
            background_image_path=background_image_path,
            offset_x=offset_x,
            offset_y=offset_y,
            add_background=add_background
        )
        
        # Clean up input file and background image
        os.remove(input_path)
        if background_image_path and os.path.exists(background_image_path):
            os.remove(background_image_path)
        
        if result['success']:
            return jsonify({
                'success': True,
                'filename': f"{timestamp}_compressed_{filename}",
                'original_size': original_size,
                'compressed_size': result['size'],
                'reduction': result['reduction'],
                'strategy': result['strategy']
            })
        else:
            return jsonify({'error': result['error']}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        
        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404
        
        response = send_file(
            file_path,
            as_attachment=True,
            download_name=filename.split('_', 1)[1] if '_' in filename else filename,
            mimetype='image/gif'
        )
        
        # Schedule file deletion after download
        @response.call_on_close
        def cleanup():
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
            except:
                pass
        
        return response
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download-batch', methods=['POST'])
def download_batch():
    try:
        filenames_json = request.form.get('filenames')
        if not filenames_json:
            return jsonify({'error': 'No filenames provided'}), 400
        
        filenames = json.loads(filenames_json)
        
        # Create a ZIP file in memory
        zip_buffer = BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for filename in filenames:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                
                if os.path.exists(file_path):
                    # Get the original filename without timestamp
                    original_name = filename.split('_', 2)[2] if filename.count('_') >= 2 else filename
                    zip_file.write(file_path, original_name)
        
        zip_buffer.seek(0)
        
        # Clean up files after creating zip
        for filename in filenames:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
            except:
                pass
        
        return send_file(
            zip_buffer,
            as_attachment=True,
            download_name='compressed_gifs.zip',
            mimetype='application/zip'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Get port from environment variable (Databricks Apps requirement)
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 for Databricks Apps
    app.run(host='0.0.0.0', port=port, debug=False)

