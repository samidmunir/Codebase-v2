import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def interpolate_arm(start: np.array, goal: np.array):
    delta_theta = np.linalg.norm(goal - start)
    
    steps = int(delta_theta / 0.1)
    
    interpolated_path = [start + (goal - start) * t for t in np.linspace(0, 1, steps)]
    
    return interpolated_path