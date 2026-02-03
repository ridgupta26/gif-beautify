# Unsplash Wallpaper Integration

## 🎨 New Features Added

### Background Selection Tabs
The background chooser now has **two tabs**:

1. **Gradients Tab** (default)
   - 8 beautiful gradient presets
   - Purple Dream, Pink Sunset, Ocean Blue, Fresh Mint, etc.
   - Plus solid White and Black options

2. **Wallpapers Tab**
   - **Mac Wallpapers** section with 6 stunning macOS-style wallpapers
   - **Gradient Wallpapers** section with 6 beautiful gradient photos
   - All sourced from Unsplash

## 📷 Wallpaper Sources

### Mac Wallpapers
High-quality wallpapers inspired by macOS:
- Abstract colorful designs
- Nature-inspired patterns
- Modern gradient aesthetics

### Gradient Wallpapers
Beautiful gradient photography from Unsplash:
- Smooth color transitions
- Artistic gradients
- Professional photography

## 🔧 How It Works

### Frontend
- **Tab switching** between Gradients and Wallpapers
- **Visual selection** - click any gradient or wallpaper to select
- **Live preview** - see the background in real-time
- **Active state** - selected item is highlighted with blue border

### Backend
1. User selects a wallpaper from Unsplash
2. Backend downloads the image (800px width for quality)
3. Image is resized to match canvas dimensions
4. Applied to GIF frames just like gradients
5. Temporary background image is cleaned up after processing

### Performance
- **Optimized download**: Only 800px width images (smaller, faster)
- **Cached for all frames**: Background loaded once, reused for all frames
- **Smart fallback**: If download fails, falls back to gradient
- **Automatic cleanup**: Temporary files deleted after processing

## 🎯 User Experience

### Selection
1. Click "Background" checkbox to enable backgrounds
2. Choose between **Gradients** or **Wallpapers** tabs
3. Click any option to select it
4. See live preview in the main panel
5. Adjust padding to add spacing around your GIF

### Export
- The wallpaper background is embedded into the final GIF
- Works with all other features (rounded corners, padding, etc.)
- Maintains aspect ratio of the original wallpaper
- High quality output

## 🚀 Benefits

1. **More variety** - Choose from gradients or photos
2. **Professional look** - Real photography backgrounds
3. **Easy to use** - Simple tabbed interface
4. **Fast performance** - Optimized downloads and caching
5. **Safe** - Automatic cleanup and error handling

## 📝 Technical Details

### Image Loading
- Uses Unsplash CDN for fast, reliable image delivery
- Thumbnail size (200x120) for selection grid
- Full size (800px) downloaded only when needed
- Converted to RGBA for proper compositing

### Supported Features
- ✅ Works with rounded corners
- ✅ Works with padding/offsets
- ✅ Works with all compression strategies
- ✅ Compatible with all GIF sizes
- ✅ Live preview support

### Error Handling
- Network timeout (10 seconds)
- Graceful fallback to gradients
- Console logging for debugging
- User-friendly error messages

