#!/bin/bash

# GIF Compressor - Drag and Drop Interface
# You can drag GIF files onto this script to compress them

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPRESS_SCRIPT="$SCRIPT_DIR/compress_gif.py"

echo "========================================================================"
echo "GIF COMPRESSOR - Drag & Drop Mode"
echo "========================================================================"
echo ""

if [ $# -eq 0 ]; then
    echo "No files provided."
    echo ""
    echo "Usage: Drag one or more GIF files onto this script"
    echo "Or run: $0 file1.gif file2.gif file3.gif"
    echo ""
    exit 1
fi

TOTAL=$#
COUNTER=0
SUCCESS=0

for gif_file in "$@"; do
    COUNTER=$((COUNTER + 1))
    
    # Check if file exists and is a GIF
    if [ ! -f "$gif_file" ]; then
        echo "[$COUNTER/$TOTAL] ✗ File not found: $gif_file"
        echo ""
        continue
    fi
    
    if [[ ! "$gif_file" =~ \.gif$ ]]; then
        echo "[$COUNTER/$TOTAL] ✗ Not a GIF file: $gif_file"
        echo ""
        continue
    fi
    
    # Generate output filename
    OUTPUT="${gif_file%.gif}_compressed.gif"
    
    echo "[$COUNTER/$TOTAL] Processing: $(basename "$gif_file")"
    echo "------------------------------------------------------------------------"
    
    if python3 "$COMPRESS_SCRIPT" "$gif_file" "$OUTPUT"; then
        SUCCESS=$((SUCCESS + 1))
        echo ""
        echo "✓ Saved to: $OUTPUT"
    fi
    
    echo ""
done

echo "========================================================================"
echo "Processing Complete!"
echo "Successfully compressed: $SUCCESS out of $TOTAL files"
echo "========================================================================"
echo ""
echo "Press Enter to close..."
read

