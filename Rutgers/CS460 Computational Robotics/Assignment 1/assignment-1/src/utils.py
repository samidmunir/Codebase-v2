import numpy as np

def euler_to_rotation_matrix(roll: float, pitch: float, yaw: float) -> np.ndarray:
    """
        Converts Euler angles (roll, pitch, yaw) to a 3 x 3 rotation matrix.
    """
    R_x = np.array(
        [
            [1, 0, 0],
            [0, np.cos(roll), -np.sin(roll)],
            [0, np.sin(roll), np.cos(roll)]
        ]
    )
    
    R_y = np.array(
        [
            [np.cos(pitch), 0, np.sin(pitch)],
            [0, -1, 0],
            [-np.sin(pitch), 0, np.cos(pitch)]
        ]
    )
    
    R_z = np.array(
        [
            [np.cos(yaw), -np.sin(yaw), 0],
            [np.sin(yaw), np.cos(yaw), 0],
            [0, 0, 1]
        ]
    )
    
    # Combine the rotations: R = R_z * R_y * R_x
    return np.dot(R_z, np.dot(R_y, R_x))