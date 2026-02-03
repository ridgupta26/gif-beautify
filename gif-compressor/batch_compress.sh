#!/bin/bash

# GIF Compressor - Batch Processing Script
# Compresses all GIF files in a directory

SCRIPT_DIR="/Users/ridhima.gupta/gif-compressor"
COMPRESS_SCRIPT="$SCRIPT_DIR/compress_gif.py"

# Default target size
TARGET_SIZE=5.0

# Check if directory is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory> [target_size_mb]"
    echo ""
    echo "Examples:"
    echo "  $0 ~/Desktop/Screenshots"
    echo "  $0 ~/Desktop/Screenshots 3.0"
    exit 1
fi

DIRECTORY="$1"
if [ $# -ge 2 ]; then
    TARGET_SIZE="$2"
fi

# Check if directory exists
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: Directory '$DIRECTORY' does not exist"
    exit 1
fi

echo "========================================================================"
echo "GIF Compressor - Batch Mode"
echo "========================================================================"
echo "Directory: $DIRECTORY"
echo "Target size: ${TARGET_SIZE}MB"
echo ""

# Count GIF files
GIF_COUNT=$(find "$DIRECTORY" -maxdepth 1 -name "*.gif" ! -name "*_compressed.gif" | wc -l)
echo "Found $GIF_COUNT GIF files to process"
echo ""

# Process each GIF
COUNTER=0
SUCCESSFUL=0
FAILED=0

find "$DIRECTORY" -maxdepth 1 -name "*.gif" ! -name "*_compressed.gif" | while read -r gif_file; do
    COUNTER=$((COUNTER + 1))
    BASENAME=$(basename "$gif_file")
    OUTPUT="${gif_file%.gif}_compressed.gif"
    
    echo "[$COUNTER/$GIF_COUNT] Processing: $BASENAME"
    echo "------------------------------------------------------------------------"
    
    if python3 "$COMPRESS_SCRIPT" "$gif_file" "$OUTPUT" "$TARGET_SIZE"; then
        SUCCESSFUL=$((SUCCESSFUL + 1))
        echo "✓ Success"
    else
        FAILED=$((FAILED + 1))
        echo "✗ Failed or warnings"
    fi
    
    echo ""
done

echo "========================================================================"
echo "Batch processing complete!"
echo "========================================================================"

