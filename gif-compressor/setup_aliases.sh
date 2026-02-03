#!/bin/bash

# Alias Setup Script for GIF Compressor
# Run this script to add convenient aliases to your shell

echo "========================================================================"
echo "GIF Compressor - Alias Setup"
echo "========================================================================"
echo ""
echo "This will add the following aliases to your ~/.zshrc:"
echo ""
echo "  gif-compress     - Compress a single GIF file"
echo "  gif-batch        - Compress all GIFs in a directory"
echo ""

# Detect shell config file
if [ -f "$HOME/.zshrc" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ -f "$HOME/.bash_profile" ]; then
    SHELL_CONFIG="$HOME/.bash_profile"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
else
    echo "Could not find shell configuration file."
    echo "Please add these aliases manually to your shell config:"
    echo ""
    echo "alias gif-compress='python3 /Users/ridhima.gupta/gif-compressor/compress_gif.py'"
    echo "alias gif-batch='/Users/ridhima.gupta/gif-compressor/batch_compress.sh'"
    exit 1
fi

echo "Will modify: $SHELL_CONFIG"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Setup cancelled."
    exit 0
fi

# Add aliases if they don't exist
if ! grep -q "gif-compress" "$SHELL_CONFIG"; then
    echo "" >> "$SHELL_CONFIG"
    echo "# GIF Compressor aliases" >> "$SHELL_CONFIG"
    echo "alias gif-compress='python3 /Users/ridhima.gupta/gif-compressor/compress_gif.py'" >> "$SHELL_CONFIG"
    echo "alias gif-batch='/Users/ridhima.gupta/gif-compressor/batch_compress.sh'" >> "$SHELL_CONFIG"
    echo ""
    echo "✓ Aliases added to $SHELL_CONFIG"
    echo ""
    echo "To use them now, run:"
    echo "  source $SHELL_CONFIG"
    echo ""
    echo "Or simply open a new terminal window."
else
    echo "✓ Aliases already exist in $SHELL_CONFIG"
fi

echo ""
echo "========================================================================"
echo "Setup Complete!"
echo "========================================================================"
echo ""
echo "Usage examples:"
echo "  gif-compress input.gif"
echo "  gif-compress input.gif output.gif"
echo "  gif-compress input.gif output.gif 3.0"
echo "  gif-batch ~/Desktop/Screenshots"
echo ""

