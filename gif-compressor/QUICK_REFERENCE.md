# Quick Reference - GIF Compressor

## Location
📁 `/Users/ridhima.gupta/gif-compressor/`

## Quick Start

### 1. Compress a Single GIF
```bash
python3 /Users/ridhima.gupta/gif-compressor/compress_gif.py input.gif
```

### 2. Set Up Easy Aliases (One-time setup)
```bash
/Users/ridhima.gupta/gif-compressor/setup_aliases.sh
```

After setup, you can use:
```bash
gif-compress input.gif
gif-batch ~/Desktop/Screenshots
```

## Common Use Cases

### Compress one GIF to under 5MB
```bash
python3 /Users/ridhima.gupta/gif-compressor/compress_gif.py ~/Desktop/Screenshots/myfile.gif
```
Output: `myfile_compressed.gif` in the same folder

### Compress with custom output name
```bash
python3 /Users/ridhima.gupta/gif-compressor/compress_gif.py input.gif output.gif
```

### Compress to under 3MB instead of 5MB
```bash
python3 /Users/ridhima.gupta/gif-compressor/compress_gif.py input.gif output.gif 3.0
```

### Compress all GIFs in a folder
```bash
/Users/ridhima.gupta/gif-compressor/batch_compress.sh ~/Desktop/Screenshots
```

## What Makes This High-Quality?

✓ **Adaptive Compression**: Tries 8 different strategies from least to most aggressive
✓ **Stops Early**: Uses the least aggressive strategy that meets target size
✓ **LANCZOS Resampling**: Highest quality resizing algorithm
✓ **Frame Preservation**: Keeps all frames if possible
✓ **Dimension Preservation**: Keeps full size if possible
✓ **Timing Preservation**: Maintains original animation speed

## Project Files

```
/Users/ridhima.gupta/gif-compressor/
├── compress_gif.py      - Main compression script
├── batch_compress.sh    - Batch process multiple GIFs
├── setup_aliases.sh     - Set up shell aliases
├── README.md            - Full documentation
└── QUICK_REFERENCE.md   - This file
```

## Requirements

- Python 3
- Pillow library (already installed)

## Tips

- Always compresses to under 5MB (or custom target)
- Maintains highest quality possible for target size
- Creates new files, never overwrites originals (unless you specify same name)
- Works best with CleanShot GIFs and screen recordings

