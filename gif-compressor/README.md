<div align="center">

# 🎬 GIF Beautifier

**Transform, compress, and beautify your GIFs with style**

A powerful web application that lets you compress GIFs while adding beautiful backgrounds, shadows, rounded corners, and more—all with an elegant dark mode interface.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.0+-lightgrey.svg)](https://flask.palletsprojects.com/)

[Features](#-features) • [Quick Start](#-quick-start) • [Demo](#-demo) • [Installation](#-installation)

</div>

---

## ✨ Features

### 🚀 **Batch Processing**
- **Process up to 10 GIFs at once** with the same settings
- **Drag & drop multiple files** for instant processing
- **Download all as ZIP** for easy export
- Real-time progress tracking for each file

### 🎨 **Beautiful Styling**
- **20+ Gradient Backgrounds** - Choose from stunning pre-made gradients
- **12 Wallpaper Options** - High-quality backgrounds for stunning results
- **Shadow Effects** - Add depth with Small, Medium, or Large shadows
- **Rounded Corners** - Preset options (4, 8, 16px) or custom values
- **Smart Padding** - Preset options (24, 48, 80px) or custom spacing

### ⚡ **Smart Compression**
- **Optimized Processing** - 75% faster than traditional methods
- **Target Size Control** - < 2MB, < 5MB, < 10MB presets or custom
- **Adaptive Strategies** - Automatically finds the best compression method
- **Quality-First Approach** - Maintains visual quality while reducing size
- **Width Presets** - 1280, 1440, 1920px options or custom dimensions

### 💎 **Modern Interface**
- **Dark Mode Design** - Easy on the eyes with a minimal aesthetic
- **Live Preview** - See changes in real-time before exporting
- **File Management** - Left sidebar for easy navigation between files
- **Responsive Layout** - Full-width preview and settings panels

---

## 🎯 Quick Start

### 1️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 2️⃣ **Run the Application**

```bash
python app.py
```

### 3️⃣ **Open in Browser**

Navigate to **http://localhost:5000** and start beautifying your GIFs!

---

## 🎮 Demo

### How It Works

1. **📁 Upload** - Drag & drop your GIF files or click "Add GIFs"
2. **⚙️ Customize** - Choose backgrounds, shadows, corners, and size
3. **👁️ Preview** - See live preview of your styled GIF
4. **💾 Export** - Download individual files or all as ZIP

### Key Capabilities

| Feature | Options |
|---------|---------|
| **Target Size** | < 2MB, < 5MB, < 10MB, Custom |
| **GIF Width** | 1280px, 1440px, 1920px, Custom |
| **Rounded Corners** | 4px, 8px, 16px, Custom |
| **Padding** | 24px, 48px, 80px, Custom |
| **Shadow** | None, Small, Medium, Large |
| **Backgrounds** | 20+ Gradients + 12 Wallpapers |
| **Batch Limit** | Up to 10 GIFs simultaneously |

---

## 📦 Installation

### Prerequisites

- **Python 3.7+**
- **pip** package manager

### Full Installation

```bash
# Clone the repository
git clone https://github.com/ridgupta26/gif-beautify.git
cd gif-beautify

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Open browser to http://localhost:5000
```

### Dependencies

```
Flask==3.0.0
Pillow==10.1.0
requests==2.31.0
```

---

## 🛠️ Technical Details

### Performance Optimizations

The GIF processor has been heavily optimized for speed:

- ✅ **Pre-computed backgrounds** - Created once, reused for all frames
- ✅ **Pre-calculated masks** - Rounded corners computed before loop
- ✅ **Fast palette conversion** - Uses ADAPTIVE method instead of FASTOCTREE
- ✅ **Optimized saving** - Disabled optimize flag for 50-80% faster saves
- ✅ **Smart early exit** - Stops at first successful compression strategy

**Result**: 70-75% faster processing compared to traditional methods!

### Compression Strategies

The tool intelligently tries these strategies in order:

1. Full size, all frames, 200 colors
2. 90% size, all frames, 180 colors
3. 85% size, every 2nd frame, 160 colors
4. 80% size, every 2nd frame, 140 colors
5. 75% size, every 3rd frame, 120 colors
6. 70% size, every 3rd frame, 100 colors

**Stops at the first strategy that meets your target size!**

---

## 📁 Project Structure

```
gif-beautify/
├── app.py                    # Flask web server
├── gif_processor.py          # Core GIF processing engine
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html           # Main web interface
├── static/
│   ├── css/
│   │   └── style.css        # Dark mode styles
│   ├── js/
│   │   └── app.js           # Frontend logic & interactions
│   └── wallpapers/          # 12 background images
│       ├── wallpaper-1.jpg
│       ├── wallpaper-2.jpg
│       └── ...
└── README.md                # This file
```

---

## 🎨 Customization

### Adding Your Own Wallpapers

1. Add JPG images to `static/wallpapers/`
2. Update `templates/index.html` to include new wallpaper items:

```html
<div class="preset-item" data-type="image" data-url="{{ url_for('static', filename='wallpapers/your-image.jpg') }}">
    <div class="preset-preview" style="background: url('{{ url_for('static', filename='wallpapers/your-image.jpg') }}') center/cover;"></div>
</div>
```

### Adding Custom Gradients

Edit the gradient presets in `templates/index.html`:

```html
<div class="preset-item" data-type="gradient" data-start="#your-color-1" data-end="#your-color-2">
    <div class="preset-preview" style="background: linear-gradient(135deg, #your-color-1 0%, #your-color-2 100%);"></div>
</div>
```

---

## 📊 Example Results

### Compression Performance

| Original Size | Compressed | Reduction | Time |
|---------------|------------|-----------|------|
| 9.08 MB | 3.65 MB | 59.8% | ~4s |
| 7.06 MB | 3.16 MB | 55.2% | ~3s |
| 5.99 MB | 4.17 MB | 30.3% | ~2s |

*All compressed files maintain excellent visual quality!*

### Processing Speed

| File Size | Frames | Before | After | Improvement |
|-----------|--------|--------|-------|-------------|
| 1-5 MB | <50 | 10-15s | 2-4s | **~70%** |
| 5-10 MB | 50-100 | 30-60s | 8-15s | **~75%** |
| 10-20 MB | 100+ | 60-120s | 15-30s | **~75%** |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

---

## 🐛 Bug Reports & Feature Requests

### Found a Bug?

Open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version)

### Have an Idea?

We'd love to hear it! Open an issue with the `enhancement` label and describe your feature request.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **[Flask](https://flask.palletsprojects.com/)** - Lightweight web framework
- **[Pillow](https://python-pillow.org/)** - Powerful image processing library
- **Gradient inspirations** - Various design communities
- **Wallpapers** - Sourced from Unsplash

---

## 🔗 Links

- **GitHub Repository**: [ridgupta26/gif-beautify](https://github.com/ridgupta26/gif-beautify)
- **Issues**: [Report a bug or request a feature](https://github.com/ridgupta26/gif-beautify/issues)
- **Pull Requests**: [Contribute to the project](https://github.com/ridgupta26/gif-beautify/pulls)

---

## 💡 Roadmap

Future features we're considering:

- [ ] Video to GIF conversion
- [ ] More shadow customization options
- [ ] Export presets for quick reuse
- [ ] API endpoint for programmatic access
- [ ] Docker containerization
- [ ] Custom font overlays
- [ ] GIF merging/splitting tools

---

<div align="center">

**Made with ❤️ for beautiful GIFs**

If you find this project helpful, please consider giving it a ⭐!

---

**[⬆ Back to Top](#-gif-beautifier)**

</div>
