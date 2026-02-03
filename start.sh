#!/bin/bash

# GIF Compressor - Quick Launcher
# This script starts the web application and opens it in your browser

echo "🎬 Starting GIF Compressor..."
echo ""

# Check if dependencies are installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

# Start the server
echo "🚀 Starting web server on http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Open browser after a short delay
(sleep 2 && open http://localhost:5000) &

# Start Flask app
python3 app.py

