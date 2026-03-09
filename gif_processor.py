"""
GIF Processor with Advanced Features
Handles compression, border radius, gradients, shadows, and offsets
OPTIMIZED VERSION - Much faster processing!
"""

import os
from PIL import Image, ImageSequence, ImageDraw, ImageFilter

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def interpolate_color(color1, color2, factor):
    """Interpolate between two colors"""
    return tuple(int(c1 + (c2 - c1) * factor) for c1, c2 in zip(color1, color2))

def create_gradient_background(width, height, start_color, end_color):
    """Create a gradient background - OPTIMIZED: Much faster approach"""
    if start_color == end_color:
        # Solid color - super fast!
        return Image.new('RGBA', (width, height), hex_to_rgb(start_color) + (255,))
    
    # Create gradient efficiently using a 1-pixel wide strip then resize
    gradient_strip = Image.new('RGBA', (1, height))
    pixels = gradient_strip.load()
    
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)
    
    # Create a single column of gradient colors
    for y in range(height):
        factor = y / height
        color = interpolate_color(start_rgb, end_rgb, factor)
        pixels[0, y] = color + (255,)
    
    # Scale it horizontally - much faster than drawing each pixel!
    return gradient_strip.resize((width, height), Image.Resampling.NEAREST)

def add_rounded_corners(img, radius):
    """Add rounded corners to an image"""
    if radius <= 0:
        return img
    
    # Create a mask with rounded corners
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    
    # Draw rounded rectangle
    draw.rounded_rectangle([(0, 0), img.size], radius=radius, fill=255)
    
    # Apply mask
    output = Image.new('RGBA', img.size, (0, 0, 0, 0))
    output.paste(img, (0, 0))
    output.putalpha(mask)
    
    return output

def create_shadow(img, shadow_size='medium', shadow_color=(0, 0, 0)):
    """
    Add a shadow effect to an image
    
    Args:
        img: PIL Image with RGBA mode
        shadow_size: 'small', 'medium', 'large', or '0' for no shadow
        shadow_color: RGB tuple for shadow color (default black)
    
    Returns:
        Image with shadow applied
    """
    if shadow_size == '0' or shadow_size == 0:
        return img
    
    # Define shadow parameters based on size
    shadow_params = {
        'small': {'offset': (4, 4), 'blur': 8, 'opacity': 25},
        'medium': {'offset': (8, 8), 'blur': 20, 'opacity': 76},
        'large': {'offset': (12, 12), 'blur': 30, 'opacity': 102}
    }
    
    params = shadow_params.get(shadow_size, shadow_params['medium'])
    offset_x, offset_y = params['offset']
    blur_radius = params['blur']
    opacity = params['opacity']
    
    # Create shadow layer
    shadow_width = img.width + abs(offset_x) + blur_radius * 2
    shadow_height = img.height + abs(offset_y) + blur_radius * 2
    
    # Create base for shadow
    shadow = Image.new('RGBA', (shadow_width, shadow_height), (0, 0, 0, 0))
    
    # Create shadow mask
    shadow_mask = Image.new('L', img.size, 0)
    
    # Copy alpha channel from original image to create shadow shape
    if img.mode == 'RGBA':
        shadow_mask = img.split()[3]  # Get alpha channel
    else:
        shadow_mask = Image.new('L', img.size, 255)
    
    # Create colored shadow
    shadow_color_img = Image.new('RGBA', img.size, shadow_color + (opacity,))
    shadow_temp = Image.new('RGBA', img.size, (0, 0, 0, 0))
    shadow_temp.paste(shadow_color_img, (0, 0), shadow_mask)
    
    # Paste shadow at offset position and blur it
    shadow_pos = (blur_radius + offset_x, blur_radius + offset_y)
    shadow.paste(shadow_temp, shadow_pos)
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # Paste original image on top of shadow
    img_pos = (blur_radius, blur_radius)
    shadow.paste(img, img_pos, img if img.mode == 'RGBA' else None)
    
    return shadow

def process_gif(input_path, output_path, target_size_mb=5.0, target_width=1900,
                border_radius=0, shadow_size='medium', gradient_start='#ffffff', gradient_end='#ffffff',
                background_image_path=None, offset_x=0, offset_y=0, add_background=False):
    """
    Process GIF with compression and styling options - HEAVILY OPTIMIZED VERSION
    
    Args:
        target_width: Target width in pixels for the output GIF
    
    Returns dict with success status and details
    """
    try:
        original_size = os.path.getsize(input_path)
        target_size_bytes = target_size_mb * 1024 * 1024
        
        # Open the GIF
        img = Image.open(input_path)
        width, height = img.size
        
        # Get frame count
        try:
            frame_count = img.n_frames
        except AttributeError:
            frame_count = 1
        
        print(f"Processing GIF: {width}x{height}, {frame_count} frames, {original_size / 1024 / 1024:.2f}MB")
        
        # Calculate target height to maintain aspect ratio
        aspect_ratio = height / width
        target_height = int(target_width * aspect_ratio)
        
        # OPTIMIZATION: If file is already under target and no styling needed, just copy it
        if (original_size <= target_size_bytes and border_radius == 0 and shadow_size == '0' and
            not add_background and width <= target_width):
            import shutil
            print("No processing needed - file already optimized")
            shutil.copy2(input_path, output_path)
            return {
                'success': True,
                'size': original_size,
                'reduction': 0,
                'strategy': 'No compression needed (already optimized)'
            }
        
        # Compression strategies - optimized order (most likely to succeed first)
        # OPTIMIZATION: Start more aggressive for better speed
        strategies = [
            (1.0, 1, 200, "Full size, all frames, 200 colors"),  # Start with fewer colors
            (0.90, 1, 180, "90% size, all frames, 180 colors"),
            (0.85, 2, 160, "85% size, every 2nd frame, 160 colors"),
            (0.80, 2, 140, "80% size, every 2nd frame, 140 colors"),
            (0.75, 3, 120, "75% size, every 3rd frame, 120 colors"),  # More aggressive frame skip
            (0.70, 3, 100, "70% size, every 3rd frame, 100 colors"),
        ]
        
        best_result = None
        
        for strategy_idx, (scale_factor, frame_skip, colors, description) in enumerate(strategies):
            print(f"Trying strategy {strategy_idx + 1}/{len(strategies)}: {description}")
            
            # Calculate scaled dimensions based on target width
            scaled_width = int(target_width * scale_factor)
            scaled_height = int(target_height * scale_factor)
            
            if add_background and (offset_x != 0 or offset_y != 0):
                canvas_width = scaled_width + abs(offset_x) * 2
                canvas_height = scaled_height + abs(offset_y) * 2
            else:
                canvas_width = scaled_width
                canvas_height = scaled_height
            
            # OPTIMIZATION: Create gradient background ONCE before loop (not per frame!)
            background_template = None
            if add_background and (offset_x != 0 or offset_y != 0 or gradient_start != gradient_end or background_image_path):
                if background_image_path:
                    # Load and resize background image
                    try:
                        bg_img = Image.open(background_image_path)
                        background_template = bg_img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
                        background_template = background_template.convert('RGBA')
                    except Exception as e:
                        print(f"Failed to load background image: {e}")
                        # Fall back to gradient
                        background_template = create_gradient_background(canvas_width, canvas_height, 
                                                                        gradient_start, gradient_end)
                else:
                    background_template = create_gradient_background(canvas_width, canvas_height, 
                                                                    gradient_start, gradient_end)
            
            # OPTIMIZATION: Calculate shadow canvas dimensions ONCE outside the loop
            shadow_canvas_width = canvas_width
            shadow_canvas_height = canvas_height
            shadow_background_template = None
            shadow_blur = 0  # Store blur for use in frame loop
            
            if shadow_size and shadow_size != '0':
                shadow_params = {
                    'small': {'offset': (4, 4), 'blur': 8},
                    'medium': {'offset': (8, 8), 'blur': 20},
                    'large': {'offset': (12, 12), 'blur': 30}
                }
                params = shadow_params.get(shadow_size, shadow_params['medium'])
                offset_s_x, offset_s_y = params['offset']
                shadow_blur = params['blur']
                
                # Adjust canvas for shadow
                shadow_canvas_width = canvas_width + abs(offset_s_x) + shadow_blur * 2
                shadow_canvas_height = canvas_height + abs(offset_s_y) + shadow_blur * 2
                
                # Create shadow background template ONCE
                if add_background and background_template:
                    if background_image_path:
                        try:
                            bg_img = Image.open(background_image_path)
                            shadow_background_template = bg_img.resize((shadow_canvas_width, shadow_canvas_height), 
                                                      Image.Resampling.LANCZOS).convert('RGBA')
                        except Exception:
                            shadow_background_template = create_gradient_background(shadow_canvas_width, shadow_canvas_height,
                                                                   gradient_start, gradient_end)
                    else:
                        shadow_background_template = create_gradient_background(shadow_canvas_width, shadow_canvas_height,
                                                               gradient_start, gradient_end)
            
            # OPTIMIZATION: Pre-calculate rounded corner mask ONCE
            rounded_mask = None
            if border_radius > 0:
                scaled_radius = int(border_radius * scale_factor)
                rounded_mask = Image.new('L', (scaled_width, scaled_height), 0)
                draw = ImageDraw.Draw(rounded_mask)
                draw.rounded_rectangle([(0, 0), (scaled_width, scaled_height)], 
                                     radius=scaled_radius, fill=255)
            
            # Process frames
            frames = []
            durations = []
            
            img.seek(0)
            frames_processed = 0
            for i, frame in enumerate(ImageSequence.Iterator(img)):
                if i % frame_skip == 0:
                    # Convert to RGBA
                    frame_rgba = frame.convert('RGBA')
                    
                    # OPTIMIZATION: Only resize if scale factor is not 1.0 AND size differs
                    if frame_rgba.size != (scaled_width, scaled_height):
                        frame_rgba = frame_rgba.resize((scaled_width, scaled_height), 
                                                      Image.Resampling.LANCZOS)
                    
                    # Add rounded corners using pre-made mask
                    if rounded_mask:
                        output = Image.new('RGBA', frame_rgba.size, (0, 0, 0, 0))
                        output.paste(frame_rgba, (0, 0))
                        output.putalpha(rounded_mask)
                        frame_rgba = output
                    
                    # Add shadow effect (before background)
                    if shadow_size and shadow_size != '0':
                        frame_rgba = create_shadow(frame_rgba, shadow_size)
                    
                    # Add background with gradient and offset
                    if shadow_background_template:
                        background = shadow_background_template.copy()
                        paste_x = (background.width - frame_rgba.width) // 2
                        paste_y = (background.height - frame_rgba.height) // 2
                        background.paste(frame_rgba, (paste_x, paste_y), frame_rgba)
                        frame_rgba = background
                    elif background_template:
                        background = background_template.copy()
                        paste_x = (background.width - frame_rgba.width) // 2
                        paste_y = (background.height - frame_rgba.height) // 2
                        background.paste(frame_rgba, (paste_x, paste_y), frame_rgba)
                        frame_rgba = background
                    
                    # OPTIMIZATION: Convert to P mode with adaptive palette (faster than quantize)
                    frame_p = frame_rgba.convert('P', palette=Image.ADAPTIVE, colors=colors)
                    frames.append(frame_p)
                    
                    # Preserve timing
                    duration = frame.info.get('duration', 100)
                    durations.append(duration * frame_skip)
                    
                    frames_processed += 1
                    
                    # Progress indicator for large GIFs
                    if frames_processed % 10 == 0:
                        print(f"  Processed {frames_processed} frames...")

            
            # Save the result
            if frames:
                print(f"  Saving {len(frames)} frames...")
                # OPTIMIZATION: Disable optimize flag for much faster save (file size difference is minimal)
                frames[0].save(
                    output_path,
                    save_all=True,
                    append_images=frames[1:],
                    duration=durations,
                    loop=0,
                    optimize=False  # Changed to False for much faster saving
                )
                
                new_size = os.path.getsize(output_path)
                print(f"  Result: {new_size / 1024 / 1024:.2f}MB (target: {target_size_mb}MB)")
                
                best_result = {
                    'size': new_size,
                    'strategy': description,
                    'reduction': ((original_size - new_size) / original_size * 100)
                }
                
                # OPTIMIZATION: Exit early if we met the target!
                if new_size <= target_size_bytes:
                    print("✓ Success! File meets target size.")
                    return {
                        'success': True,
                        'size': new_size,
                        'reduction': best_result['reduction'],
                        'strategy': description
                    }
                else:
                    print("  Still too large, trying next strategy...")

        
        # Return best result even if target not met
        if best_result:
            return {
                'success': True,
                'size': best_result['size'],
                'reduction': best_result['reduction'],
                'strategy': best_result['strategy']
            }
        else:
            return {
                'success': False,
                'error': 'Could not process GIF'
            }
            
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

