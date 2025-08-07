#!/usr/bin/env python3
"""
3D Planck Voxel Visualization Web Application
Startup script that installs dependencies and runs the Flask app
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False
    return True

def run_app():
    """Run the Flask application"""
    print("🚀 Starting 3D Planck Voxel Visualization...")
    print("🌐 Web interface will be available at: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        from main import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Failed to start server: {e}")

if __name__ == "__main__":
    print("🌌 3D Planck Voxel Visualization")
    print("=" * 50)
    
    if install_dependencies():
        run_app()
    else:
        print("❌ Cannot start application due to dependency installation failure")
        sys.exit(1)