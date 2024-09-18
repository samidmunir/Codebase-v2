import numpy as np
from utils import euler_to_rotation_matrix
from utils import random_quaternion
from utils import quaternion_to_rotation_matrix
from utils import visualize_rotation

def random_rotation_matrix(bool: naive) -> matrix:
    if naive:
        # Naive method: random Euler angles
        roll = np.random.uniform(0, 2 * np.pi)
        pitch = np.random.uniform(0, 2 * np.pi)
        yaw = np.random.uniform(0, 2 * np.pi)
        R = euler_to_rotation_matrix(roll, pitch, yaw)
    else:
        # Advanced method: random quaternion
        q = random_quaternion()
        R = quaternion_to_rotation_matrix(q)
        
    return R