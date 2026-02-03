# Wallpapers Directory

This directory is for your downloaded Unsplash wallpapers.

## How to Add Wallpapers

1. Download your favorite wallpapers from Unsplash
2. Rename them to `wallpaper-1.jpg`, `wallpaper-2.jpg`, etc.
3. Place them in this directory (`static/wallpapers/`)
4. The app will automatically load them in the background selection grid

## Current Setup

The app is configured to load 9 wallpapers:
- `wallpaper-1.jpg` through `wallpaper-9.jpg`

You can add more by editing the `templates/index.html` file and adding more preset items.

## File Format

- Recommended format: `.jpg` or `.jpeg`
- Recommended resolution: At least 1920x1080 for best quality
- File size: Keep under 2MB for faster loading

## Example

```
static/wallpapers/
  ├── wallpaper-1.jpg  (Your first wallpaper)
  ├── wallpaper-2.jpg  (Your second wallpaper)
  ├── wallpaper-3.jpg  (etc...)
  └── ...
```

