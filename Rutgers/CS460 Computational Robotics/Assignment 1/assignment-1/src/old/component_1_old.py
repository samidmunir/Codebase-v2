import numpy as np

"""
function check_SOn()
    This function should determine whether a given matrix belongs to
     the Speical Orthogonal Group, denoted as SO(n).
    A matrix in SO(n) must satisfy the following 2 conditions:
     - Orthogonality: The matrix m must be orthogonal, meaning
        m^T * m = I, where I is the identity matrix, and m^T is the 
        transpose of m.
     - Determinant: The determinant of m must be 1.
"""
def check_SOn(m: np.ndarray, epsilon: float = 0.01) -> bool:
    # Checking if matrix is a square.
    if m.shape[0] != m.shape[1]:
        return False
    
    # Checking the orthogonality condition.
    # --> m.T * m = I
    identity = np.eye(m.shape[0]) # Computing identity matrix.
    orthogonality_check = np.allclose(np.dot(m.T, m), identity, atol = epsilon)
    
    # Checking if the determinant is close to 1.
    determinant_check = np.isclose(np.linalg.det(m), 1.0, atol = epsilon)
    
    # Both checks must pass for matrix to bleong to SO(n).
    return orthogonality_check and determinant_check

"""
function check_quaternion()
    This function is designed to determine whether a given vector 
     represents a valid quaternion. Specifically, a quaternion is valid
     if its norm (or length) is equal to 1, meaning it's a unit
     quaternion.
    The quaternion's norm must be 1 to ensure that it represents a pure
     rotation without any scaling.
"""
def check_quaternion(v: list, epsilon: float = 0.01) -> bool:
    # Converting list to numpy array (in case it's not).
    v = np.array(v)
    
    # Calculating the norm of the quaternion.
    # --> Function norm() computes the Euclidean (L2) norm of the 
    #       vector v.
    # E.g., quaternion q = [q0, q1, q2, q3]
    #       --> norm(q) = sqrt((q0 ** q0) + (q1 ** q1) + (q2 ** q2) + (q3 ** q3))
    norm = np.linalg.norm(v)
    
    # Checking if the norm is close to 1.
    return np.isclose(norm, 1.0, atol = epsilon)

"""
function check_SEn()
    This function checks if a given matrix belongs to the Special
     Euclidean Group, denoted as SE(n). This group describes rigid
     body transformations in n-dimensional space, combing rotation
     and translation. In 2D and 3D spaces, matrices in SE(n)
     typically represent transformations that consist of:
     - a rotation matrix in SO(n) (the rotation part).
     - a translation vector (the translation part).
     - the last row of the matrix is for homogeneity.
"""
def check_SEn(m: np.ndarray, epsilon: float = 0.01) -> bool:
    # Checking if the matrix has the correct shape (n + 1, n + 1).
    n = m.shape[0] - 1
    if m.shape[0] != m.shape[1] or (n not in [2, 3]):
        return False
    
    # Extracting the rotation matrix (top-left n x n part).
    rotation_matrix = m[:n, :n]
    
    # Checking if the rotation matrix is in SO(n).
    if not check_SOn(rotation_matrix, epsilon):
        return False
    
    # Checking if the last row [0, ..., 1] (for homogeneity).
    # --> for n = 2, last row: [0, 0, 1]
    # --> for n = 3, last row: [0, 0, 0, 1]
    last_row_check = np.allclose(m[n, :], np.append(np.zeros(n), 1), atol = epsilon)
    
    return last_row_check