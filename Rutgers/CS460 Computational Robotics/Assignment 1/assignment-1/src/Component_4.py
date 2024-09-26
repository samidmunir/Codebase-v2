import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def interpolate_arm(start: np.array, goal: np.array) -> np.ndarray:
    delta_theta = np.linalg.norm(goal - start)
    
    steps = int(delta_theta / 0.1)
    
    interpolated_path = [start + (goal - start) * t for t in np.linspace(0, 1, steps)]
    
    return interpolated_path

def forward_propagate_arm(start_pose: np.array, plan: np.ndarray) -> np.ndarray:
    path = [start_pose]
    
    for velocity, duration in plan:
        last_pose = np.array(path[-1])
        delta_theta = np.array(velocity) * duration
        new_pose = last_pose + delta_theta
        
        path.append(new_pose)
    
    return path