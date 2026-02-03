#!/usr/bin/env python3
"""
High-Quality GIF Compressor
Compresses GIF files to under 5MB while maintaining the highest possible quality
"""

import os
import sys
from PIL import Image, ImageSequence

def compress_gif_adaptive(input_path, output_path, target_size_mb=5.0, max_attempts=5):
    """
    Adaptively compress a GIF file to meet target size while maintaining quality
    
    This function tries multiple compression strategies, starting with the least
    aggressive (highest quality) and progressively applying more compression
    only if needed to reach the target size.
    
    Args:
        input_path: Path to input GIF
        output_path: Path to output GIF
        target_size_mb: Target file size in MB (default: 5.0)
        max_attempts: Maximum number of compression attempts
    """
    original_size = os.path.getsize(input_path)
    target_size_bytes = target_size_mb * 1024 * 1024
    
    print("="*70)
    print(f"HIGH-QUALITY GIF COMPRESSOR")
    print("="*70)
    print(f"Original file: {input_path}")
    print(f"Original size: {original_size / (1024*1024):.2f} MB")
    print(f"Target size: {target_size_mb} MB")
    
    # If already under target, just optimize
    if original_size <= target_size_bytes:
        print(f"\n✓ File is already under {target_size_mb} MB!")
        print("Applying lossless optimization only...")
        img = Image.open(input_path)
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            optimize=True
        )
        new_size = os.path.getsize(output_path)
        print(f"Optimized size: {new_size / (1024*1024):.2f} MB")
        return True
    
    # Open the GIF
    img = Image.open(input_path)
    width, height = img.size
    print(f"Original dimensions: {width}x{height}")
    
    # Count frames
    frame_count = sum(1 for _ in ImageSequence.Iterator(img))
    print(f"Frame count: {frame_count}")
    
    # Compression strategies (from least to most aggressive)
    # Each strategy: (scale_factor, frame_skip, colors, description)
    strategies = [
        (1.0, 1, 256, "Full size, all frames, 256 colors"),
        (0.95, 1, 256, "95% size, all frames, 256 colors"),
        (0.90, 1, 256, "90% size, all frames, 256 colors"),
        (0.85, 1, 256, "85% size, all frames, 256 colors"),
        (0.85, 2, 256, "85% size, every 2nd frame, 256 colors"),
        (0.80, 2, 256, "80% size, every 2nd frame, 256 colors"),
        (0.75, 2, 220, "75% size, every 2nd frame, 220 colors"),
        (0.70, 2, 200, "70% size, every 2nd frame, 200 colors"),
    ]
    
    print(f"\nTrying compression strategies (starting with highest quality)...")
    print("-"*70)
    
    for attempt, (scale_factor, frame_skip, colors, description) in enumerate(strategies[:max_attempts], 1):
        print(f"\nAttempt {attempt}: {description}")
        
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        
        # Extract and process frames
        frames = []
        durations = []
        
        img.seek(0)  # Reset to first frame
        for i, frame in enumerate(ImageSequence.Iterator(img)):
            if i % frame_skip == 0:
                # Convert to RGBA for high-quality resizing
                frame_rgba = frame.convert('RGBA')
                
                # Use LANCZOS for high-quality downsampling
                if scale_factor < 1.0:
                    frame_resized = frame_rgba.resize((new_width, new_height), Image.Resampling.LANCZOS)
                else:
                    frame_resized = frame_rgba
                
                # Convert to palette mode with adaptive color selection
                frame_p = frame_resized.convert('P', palette=Image.ADAPTIVE, colors=colors)
                frames.append(frame_p)
                
                # Preserve frame timing
                duration = frame.info.get('duration', 100)
                durations.append(duration * frame_skip)
        
        extracted_frames = len(frames)
        
        # Save with optimization
        try:
            frames[0].save(
                output_path,
                save_all=True,
                append_images=frames[1:],
                duration=durations,
                loop=0,
                optimize=True,
                quality=95  # High quality setting
            )
            
            new_size = os.path.getsize(output_path)
            reduction_percent = ((original_size - new_size) / original_size * 100)
            
            print(f"  → Dimensions: {new_width}x{new_height}")
            print(f"  → Frames: {extracted_frames}")
            print(f"  → Size: {new_size / (1024*1024):.2f} MB ({reduction_percent:.1f}% reduction)")
            
            if new_size <= target_size_bytes:
                print(f"\n{'='*70}")
                print(f"✓ SUCCESS! Compressed to {new_size / (1024*1024):.2f} MB (under {target_size_mb} MB)")
                print(f"{'='*70}")
                print(f"Strategy used: {description}")
                print(f"Final dimensions: {new_width}x{new_height}")
                print(f"Final frame count: {extracted_frames} (from {frame_count} original)")
                print(f"Size reduction: {reduction_percent:.1f}%")
                print(f"\nOutput saved to: {output_path}")
                return True
            else:
                print(f"  ✗ Still {(new_size - target_size_bytes) / (1024*1024):.2f} MB over target")
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
            continue
    
    # If we get here, we couldn't meet the target
    print(f"\n{'='*70}")
    print(f"⚠ WARNING: Could not compress to under {target_size_mb} MB")
    print(f"{'='*70}")
    final_size = os.path.getsize(output_path)
    print(f"Best result: {final_size / (1024*1024):.2f} MB")
    print(f"This is the highest quality possible close to your target.")
    return False

def main():
    print("\n" + "="*70)
    print("HIGH-QUALITY GIF COMPRESSOR")
    print("Always maintains quality while targeting < 5MB file size")
    print("="*70 + "\n")
    
    if len(sys.argv) < 2:
        print("Usage: python3 compress_gif.py <input.gif> [output.gif] [target_size_mb]")
        print("\nExamples:")
        print("  python3 compress_gif.py input.gif")
        print("  python3 compress_gif.py input.gif output.gif")
        print("  python3 compress_gif.py input.gif output.gif 5.0")
        print("\nThe script will automatically try multiple compression levels,")
        print("starting with the highest quality and stopping as soon as the")
        print("target size is achieved.")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.gif', '_compressed.gif')
    target_size_mb = float(sys.argv[3]) if len(sys.argv) > 3 else 5.0
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    if output_file == input_file:
        # Create a backup
        backup_file = input_file.replace('.gif', '_original.gif')
        output_file = input_file
        print(f"⚠ Note: Will overwrite original. Creating backup at: {backup_file}")
        import shutil
        shutil.copy2(input_file, backup_file)
        input_file = backup_file
    
    success = compress_gif_adaptive(input_file, output_file, target_size_mb)
    
    if success:
        print(f"\n✓ Compression complete!")
        return 0
    else:
        print(f"\n⚠ Compression completed with warnings.")
        print(f"File size may be slightly over target, but quality is maximized.")
        return 0

if __name__ == "__main__":
    sys.exit(main())

