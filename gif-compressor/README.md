# ✨ GIF Beautifier

<div align="center">

**Transform, Compress & Style Your GIFs**

Beautify your GIFs with custom backgrounds, shadows, rounded corners, and smart compression - all in one powerful tool.

[Features](#features) • [Installation](#installation) • [Usage](#usage)

</div>

---

## ✨ Features

### 🎯 Smart Compression
- **Adaptive Algorithms**: Automatically tries 8 different compression strategies
- **Quality-First**: Starts with highest quality and only applies more compression if needed
- **Target Size Control**: Set custom target file sizes (< 2MB, < 5MB, < 10MB, or custom)
- **Batch Processing**: Compress up to 10 GIFs at once with the same settings
- **LANCZOS Resampling**: Uses the best resizing algorithm for superior quality

### 🎨 Style Customization
- **Rounded Corners**: Add elegant rounded corners with preset values or custom radius
- **Shadow Effects**: Choose from Small, Medium, or Large shadow styles for depth
- **Gradient Backgrounds**: Select from 14 beautiful pre-made gradients
- **Wallpaper Backgrounds**: Use stunning Unsplash wallpapers as backgrounds
- **Custom Padding**: Add precise padding around your GIFs
- **Multiple Sizes**: Choose from preset widths (1280, 1440, 1920) or set custom dimensions

### 💻 Two Ways to Use
1. **Web Interface**: Beautiful, modern UI for drag-and-drop compression
2. **Command Line**: Python script for batch processing and automation

---

## 🚀 Quick Start

### Web Interface

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run the app**:
```bash
python app.py
```

3. **Open your browser**:
```
http://localhost:5000
```

### Command Line

```bash
# Simple compression
python compress_gif.py input.gif

# Custom settings
python compress_gif.py input.gif output.gif 3.0
```

---

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step-by-Step

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/gif-compressor.git
cd gif-compressor
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the application**:
```bash
# Web interface
python app.py

# Or use command line
python compress_gif.py your-file.gif
```

---

## 🎮 Usage

### Web Interface

1. **Upload your GIF** - Drag & drop or click to browse
2. **Adjust settings**:
   - Target file size (1-10 MB)
   - Border radius (0-50 px)
   - Background gradient colors
   - Horizontal/vertical offsets
3. **Click "Compress GIF"**
4. **Download your compressed file**

### Command Line Interface

#### Basic Usage
```bash
python compress_gif.py input.gif
```
Output: `input_compressed.gif`

#### With Custom Output
```bash
python compress_gif.py input.gif output.gif
```

#### Custom Target Size
```bash
python compress_gif.py input.gif output.gif 3.0
```

#### Batch Processing
```bash
# Process all GIFs in a folder
./batch_compress.sh ~/Desktop/Screenshots

# Or drag multiple files
./drag_and_drop.sh file1.gif file2.gif file3.gif
```

---

## 🛠️ Configuration

### Compression Strategies

The tool automatically tries these strategies in order:

1. Full size, all frames, 256 colors
2. 95% size, all frames, 256 colors
3. 90% size, all frames, 256 colors
4. 85% size, all frames, 256 colors
5. 85% size, every 2nd frame, 256 colors
6. 80% size, every 2nd frame, 256 colors
7. 75% size, every 2nd frame, 220 colors
8. 70% size, every 2nd frame, 200 colors

It stops at the first strategy that meets your target size!

---

## 📊 Examples

### Before & After

| Original | Compressed | Reduction |
|----------|------------|-----------|
| 9.08 MB  | 3.65 MB    | 59.8%     |
| 7.06 MB  | 3.16 MB    | 55.2%     |
| 5.99 MB  | 4.17 MB    | 30.3%     |

All compressed files maintain high visual quality!

---

## 🏗️ Project Structure

```
gif-compressor/
├── app.py                    # Flask web application
├── gif_processor.py          # Core compression & styling logic
├── compress_gif.py           # Command-line interface
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── templates/
│   └── index.html           # Web interface HTML
├── static/
│   ├── css/
│   │   └── style.css        # Styles
│   └── js/
│       └── app.js           # Frontend JavaScript
├── batch_compress.sh        # Batch processing script
├── drag_and_drop.sh         # Drag & drop interface
└── setup_aliases.sh         # Alias setup script
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](#) file for details.

---

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) and [Pillow](https://python-pillow.org/)
- Inspired by the need for high-quality GIF compression
- Designed with modern web standards and best practices

---

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)

---

## 💡 Feature Requests

Have an idea? Open an issue with the `enhancement` label!

---

## 📧 Contact

- GitHub: [@yourusername](https://github.com/yourusername)
- Project Link: [https://github.com/yourusername/gif-compressor](https://github.com/yourusername/gif-compressor)

---

<div align="center">

**Made with ❤️ for high-quality GIF compression**

⭐ Star this repo if you find it helpful!

</div>
