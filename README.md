# 🌌 3D Planck Voxel Visualization

A beautiful web application for visualizing quantum fluctuations in a 3D spatial grid over time. This interactive tool allows you to explore how binary states evolve in a 10×10×10 voxel grid through 20 time steps.

## 🚀 Quick Start

### Option 1: Automatic Setup (Recommended)
```bash
python run.py
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

The web interface will be available at: **http://localhost:5000**

## ✨ Features

- **🎲 Interactive Simulation**: Generate new random simulations with a single click
- **⏰ Time Navigation**: Explore different time steps using an interactive slider
- **🌌 3D Visualization**: Beautiful 3D voxel renderings with blue active states and white inactive states
- **📊 Real-time Updates**: Dynamic visualization updates without page refresh
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **🎨 Modern UI**: Beautiful gradient design with smooth animations

## 🔬 Simulation Parameters

- **Grid Size**: 10×10×10 voxels (1000 total spatial points)
- **Time Steps**: 20 ticks for temporal evolution
- **Fluctuation Probability**: 5% chance of state change per voxel per time step
- **Visualization**: Blue voxels = active states, White voxels = inactive states

## 🎮 How to Use

1. **Generate Simulation**: Click "🎲 Generate New Simulation" to create a new random evolution
2. **View Time Steps**: The app automatically shows three key moments:
   - Initial state (t=0)
   - Midpoint (t=10)
   - Final state (t=19)
3. **Explore Specific Times**: Use the time slider to visualize any specific time step
4. **Interactive Controls**: Click "🔄 Visualize Current Time" to generate custom time step views

## 🛠️ Technical Details

### Backend
- **Framework**: Flask (Python)
- **Visualization**: Matplotlib with 3D voxel rendering
- **Data Processing**: NumPy for efficient array operations
- **Image Encoding**: Base64 encoding for web delivery

### Frontend
- **Pure HTML/CSS/JavaScript**: No external frameworks required
- **Responsive Grid Layout**: CSS Grid for adaptive visualization cards
- **Smooth Animations**: CSS transitions and keyframes
- **Modern Design**: Glassmorphism effects and gradient backgrounds

### API Endpoints
- `GET /`: Main web interface
- `POST /generate`: Generate new simulation with visualizations
- `POST /visualize/<time>`: Generate visualization for specific time step

## 📦 Dependencies

- Flask 2.3.3
- NumPy 1.24.3
- Matplotlib 3.7.2
- Werkzeug 2.3.7

## 🌟 What You'll See

The application simulates a quantum-like system where:
- Each voxel can be in one of two states (0 or 1)
- States randomly fluctuate over time with 5% probability
- The 3D visualization shows the spatial distribution of active states
- You can observe how patterns evolve and change over 20 time steps

This creates an engaging visualization of emergent complexity from simple probabilistic rules, similar to cellular automata but in 3D space with temporal evolution.

## 🎯 Perfect For

- **Physics Education**: Understanding quantum fluctuations and probabilistic systems
- **Data Visualization**: Learning about 3D data representation
- **Interactive Learning**: Exploring complex systems through visualization
- **Research**: Prototyping ideas for 3D cellular automata or quantum simulations

---

*Enjoy exploring the fascinating world of 3D quantum fluctuations! 🌌*
