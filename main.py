from flask import Flask, render_template, request, jsonify, send_file
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import io
import base64
import os

app = Flask(__name__)

# Grid and Simulation Settings
GRID_SIZE = (10, 10, 10)    # 3D spatial grid size (x, y, z)
TICKS = 20                  # Total time steps (t)
PROB_FLUCTUATION = 0.05     # Probability of spontaneous state change

def generate_simulation():
    """Generate the 3D Planck voxel simulation"""
    # Create empty 4D grid: x, y, z, time
    grid = np.zeros((*GRID_SIZE, TICKS), dtype=int)
    
    # Initialize t=0 with random binary states (0 or 1)
    grid[..., 0] = np.random.choice([0, 1], size=GRID_SIZE, p=[1 - PROB_FLUCTUATION, PROB_FLUCTUATION])
    
    # Simple evolution rule: random fluctuation over time
    for t in range(1, TICKS):
        prev = grid[..., t - 1]
        flip = np.random.rand(*GRID_SIZE) < PROB_FLUCTUATION
        grid[..., t] = np.where(flip, 1 - prev, prev)
    
    return grid

def visualize_voxels(grid, t):
    """Create 3D voxel visualization for a selected time step"""
    assert 0 <= t < TICKS, "Time step out of bounds"
    
    state = grid[..., t]
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    filled = state.astype(bool)
    colors = np.where(filled, 'blue', 'white')
    
    ax.voxels(filled, facecolors=colors, edgecolor='k', linewidth=0.4)
    ax.set_title(f"3D Planck Voxel Grid at t = {t}")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Convert plot to base64 string
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight')
    img_buffer.seek(0)
    plt.close()
    
    img_str = base64.b64encode(img_buffer.getvalue()).decode()
    return img_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Generate a new simulation and return visualization"""
    try:
        grid = generate_simulation()
        
        # Generate visualizations for different time steps
        t0_img = visualize_voxels(grid, 0)
        t_mid_img = visualize_voxels(grid, TICKS // 2)
        t_final_img = visualize_voxels(grid, TICKS - 1)
        
        return jsonify({
            'success': True,
            't0': t0_img,
            't_mid': t_mid_img,
            't_final': t_final_img,
            'total_ticks': TICKS
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/visualize/<int:t>', methods=['POST'])
def visualize_at_time(t):
    """Generate visualization for a specific time step"""
    try:
        grid = generate_simulation()
        img_str = visualize_voxels(grid, t)
        return jsonify({'success': True, 'image': img_str})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)