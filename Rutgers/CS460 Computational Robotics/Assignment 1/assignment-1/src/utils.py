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

def random_quaternion() -> np.ndarray:
    """
        Generate a random unit quaternion.
    """
    u1, u2, u3 = np.random.uniform(0, 1, 3)
    q1 = np.sqrt(1 - u1) * np.sin(2 * np.pi * u2)
    q2 = np.sqrt(1 - u1) * np.cos(2 * np.pi * u2)
    q3 = np.sqrt(u1) * np.sin(2 * np.pi * u3)
    q4 = np.sqrt(u1) * np.cos(2 * np.pi * u3)
    
    return np.array([q1, q2, q3, q4])

def quaternion_to_rotation_matrix(q: np.ndarray) -> np.ndarray:
    """
        Convert a quaternion (q1, q2, q3, q4) into a 3 x 3 rotation matrix.
    """
    q1, q2, q3, q4 = q
    return np.array(
        [
            [1 - 2 * (q3 ** 2 + q4 ** 2), 2 * (q2 * q3 - q1 * q4), 2 * (q2 * q4 + q1 * q3)],
            [2 * (q2 * q3 + q1 * q4), 1 - 2 * (q2 ** 2 + q4 ** 2), 2 * (q3 * q4 - q1 * q2)],
            [2 * (q2 * q4 - q1 * q3), 2 * (q3 * q4 + q1 * q2), 1 - 2 * (q2 ** 2 + q3 ** 2)]
        ]
    )