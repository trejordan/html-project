#!/bin/bash

echo "🌌 3D Planck Voxel Visualization"
echo "=================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install dependencies
echo "📦 Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Start the application
echo "🚀 Starting the application..."
echo "🌐 Web interface will be available at: http://localhost:5000"
echo "⏹️  Press Ctrl+C to stop the server"
echo "----------------------------------------"

python main.py