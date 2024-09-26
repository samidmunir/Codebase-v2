import numpy as np
from scipy.spatial.transform import Rotation as R
from utils import euler_to_rotation_matrix
from utils import random_quaternion
from utils import quaternion_to_rotation_matrix
from utils import visualize_rotation, visualize_rotation_v2
from old.component_1_old import check_SOn

def random_rotation_matrix_v1(naive: bool) -> np.ndarray:
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

def random_rotation_matrix_v2(naive: bool) -> np.ndarray:
    if naive:
        # Naive method: generate random Euler angles and convert to
        #  rotation matrix.
        angles = np.random.uniform(0, 2 * np.pi, 3) # Random yaw, pitch, roll.
        rotation = R.from_euler('xyz', angles) # Convert Euler angles to rotation matrix.
        rotation_matrix = rotation.as_matrix()
    else:
        # Sophisticated method: generate a random quaternion.
        random_quaternion = np.random.normal(size = 4) # Generate random numbers for quaternion.
        random_quaternion /= np.linalg.norm(random_quaternion) # Normalize the unit quaternion.
        rotation = R.from_quat(random_quaternion) # Convert quaternion to rotation matrix.
        rotation_matrix = rotation.as_matrix()
    
    if check_SOn(rotation_matrix):
        return rotation_matrix
    else:
        raise ValueError('Generated matrix does not belong to SO(n).')