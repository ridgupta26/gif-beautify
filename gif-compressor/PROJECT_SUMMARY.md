# 🎬 GIF Compressor Project

**High-quality GIF compression that always keeps files under 5MB**

---

## 📍 Project Location

```
/Users/ridhima.gupta/gif-compressor/
```

---

## 🚀 Quick Start (Choose Your Method)

### Method 1: Direct Command (Works Immediately)
```bash
python3 /Users/ridhima.gupta/gif-compressor/compress_gif.py your-file.gif
```

### Method 2: Set Up Aliases (One-time, Then Super Easy)
```bash
# Run setup once
/Users/ridhima.gupta/gif-compressor/setup_aliases.sh

# Then use anywhere
gif-compress your-file.gif
```

### Method 3: Drag & Drop (Most Convenient)
```bash
# Navigate to project folder in Finder
open /Users/ridhima.gupta/gif-compressor/

# Drag GIF files onto drag_and_drop.sh
```

---

## ✨ Key Features

### 🎯 Always Under 5MB
Every GIF will be compressed to under 5MB (or your custom target)

### 🏆 Highest Quality Possible
- Uses 8 adaptive compression strategies
- Starts with highest quality (full size, all frames)
- Only applies more compression if needed
- LANCZOS resampling for best resize quality

### 🛡️ Safe & Non-Destructive
- Never overwrites originals
- Creates `_compressed.gif` versions
- Shows before/after comparison

### ⚡ Smart & Efficient
- Automatically finds the best compression level
- Preserves frame timing
- Maintains animation smoothness

---

## 📚 Usage Examples

### Basic Compression
```bash
# Compress to under 5MB
python3 /Users/ridhima.gupta/gif-compressor/compress_gif.py input.gif

# Output: input_compressed.gif
```

### Custom Output Name
```bash
python3 /Users/ridhima.gupta/gif-compressor/compress_gif.py input.gif output.gif
```

### Custom Target Size
```bash
# Compress to under 3MB instead of 5MB
python3 /Users/ridhima.gupta/gif-compressor/compress_gif.py input.gif output.gif 3.0
```

### Batch Process Entire Folder
```bash
/Users/ridhima.gupta/gif-compressor/batch_compress.sh ~/Desktop/Screenshots
```

### Process Multiple Files
```bash
/Users/ridhima.gupta/gif-compressor/drag_and_drop.sh file1.gif file2.gif file3.gif
```

---

## 📊 Compression Strategies (Tried in Order)

The script automatically tries these strategies and stops at the first one that meets your target:

1. ✅ **Full size, all frames, 256 colors** (Best Quality)
2. ✅ 95% size, all frames, 256 colors
3. ✅ 90% size, all frames, 256 colors
4. ✅ 85% size, all frames, 256 colors
5. ✅ 85% size, every 2nd frame, 256 colors
6. ✅ 80% size, every 2nd frame, 256 colors
7. ✅ 75% size, every 2nd frame, 220 colors
8. ✅ 70% size, every 2nd frame, 200 colors

---

## 📁 Project Files

```
/Users/ridhima.gupta/gif-compressor/
│
├── 🐍 compress_gif.py         Main compression script
├── 📦 batch_compress.sh       Process entire folders
├── 🎯 drag_and_drop.sh        Drag & drop interface
├── ⚙️  setup_aliases.sh        One-time alias setup
├── 📖 README.md               Full documentation
├── 📋 QUICK_REFERENCE.md      Quick command reference
└── 📄 PROJECT_SUMMARY.md      This file
```

---

## 🔧 Requirements

- ✅ Python 3 (already installed)
- ✅ Pillow library (already installed)

---

## 💡 Tips & Tricks

### Tip 1: Fastest Workflow
Set up aliases once, then use from anywhere:
```bash
cd ~/Desktop/Screenshots
gif-compress myfile.gif
```

### Tip 2: Batch Processing
Process all GIFs in a folder at once:
```bash
gif-batch ~/Desktop/Screenshots
```

### Tip 3: Custom Target Size
Need smaller files for email (e.g., 2MB limit)?
```bash
gif-compress input.gif output.gif 2.0
```

### Tip 4: Check Results
The script shows:
- Original size vs compressed size
- Percentage reduction
- Dimensions and frame count
- Which strategy was used

---

## 🎉 Real Results From Your GIFs

### Test 1: CleanShot 2026-02-03 at 10.46.06.gif
- **Before**: 5.99 MB (2000×1034, 166 frames)
- **After**: 4.17 MB (2000×1034, 166 frames)
- **Strategy**: Full size, all frames maintained!
- **Reduction**: 30.3%

### Test 2: CleanShot 2026-02-02 at 14.31.03.gif
- **Before**: 7.06 MB (2000×1149, 215 frames)
- **After**: 3.16 MB (1700×976, 108 frames)
- **Reduction**: 55.2%

### Test 3: CleanShot 2026-02-03 at 10.56.15.gif
- **Before**: 9.08 MB (2000×1148, 158 frames)
- **After**: 3.65 MB (1700×975, 79 frames)
- **Reduction**: 59.8%

---

## 🆘 Help & Support

### View Full Documentation
```bash
cat /Users/ridhima.gupta/gif-compressor/README.md
```

### View Quick Reference
```bash
cat /Users/ridhima.gupta/gif-compressor/QUICK_REFERENCE.md
```

### Open Project Folder
```bash
open /Users/ridhima.gupta/gif-compressor/
```

---

## 🎯 Common Commands (Bookmark These!)

```bash
# Compress one GIF
python3 ~/gif-compressor/compress_gif.py input.gif

# Compress entire folder
~/gif-compressor/batch_compress.sh ~/Desktop/Screenshots

# Set up easy aliases (one time)
~/gif-compressor/setup_aliases.sh

# After alias setup
gif-compress input.gif
gif-batch ~/Desktop/Screenshots
```

---

**Made with ❤️ for high-quality GIF compression**

*Your GIFs deserve to look great AND be under 5MB!*

