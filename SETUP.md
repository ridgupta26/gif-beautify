# GIF Compressor - Setup Guide

## Quick Setup (5 minutes)

### 1. Install Python Dependencies

```bash
cd /Users/ridhima.gupta/gif-compressor
pip3 install -r requirements.txt
```

### 2. Run the Web Application

```bash
python3 app.py
```

The app will start on `http://localhost:5000`

### 3. Open in Browser

Visit: http://localhost:5000

---

## For GitHub

### 1. Initialize Git Repository

```bash
cd /Users/ridhima.gupta/gif-compressor
git init
git add .
git commit -m "Initial commit: GIF Compressor with web UI"
```

### 2. Create GitHub Repository

1. Go to https://github.com/new
2. Name it: `gif-compressor`
3. Don't initialize with README (we have one)
4. Click "Create repository"

### 3. Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/gif-compressor.git
git branch -M main
git push -u origin main
```

### 4. Update README Links

Before pushing, update these in `README.md`:
- Replace `yourusername` with your actual GitHub username
- Update the GitHub links

---

## Usage

### Web Interface

1. Start the server: `python3 app.py`
2. Open browser: `http://localhost:5000`
3. Upload a GIF
4. Adjust settings (size, border radius, gradient, etc.)
5. Click "Compress GIF"
6. Download your result!

### Command Line

```bash
# Simple compression
python3 compress_gif.py input.gif

# With options
python3 compress_gif.py input.gif output.gif 3.0
```

---

## Features Overview

### Compression Settings
- **Target Size**: 1-10 MB (default: 5MB)
- **Auto-optimize**: Tries 8 strategies for best quality

### Style Settings
- **Border Radius**: 0-50px rounded corners
- **Background**: Toggle gradient background
- **Gradient Colors**: Custom start and end colors
- **Offsets**: Horizontal and vertical padding

---

## Troubleshooting

### Port Already in Use

If port 5000 is busy, change it in `app.py`:
```python
app.run(debug=True, port=5001)  # Use different port
```

### Module Not Found

```bash
pip3 install -r requirements.txt
```

### Permission Denied

```bash
chmod +x compress_gif.py batch_compress.sh
```

---

## Project Structure

```
gif-compressor/
├── app.py              # Flask web server
├── gif_processor.py    # Core compression logic
├── compress_gif.py     # CLI tool
├── requirements.txt    # Dependencies
├── templates/          # HTML templates
│   └── index.html
├── static/            # CSS & JavaScript
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
└── README.md          # Documentation
```

---

## Next Steps

1. ✅ Test the web interface
2. ✅ Try different compression settings
3. ✅ Upload to GitHub
4. ✅ Share with others!

---

**Need help?** Open an issue on GitHub!

