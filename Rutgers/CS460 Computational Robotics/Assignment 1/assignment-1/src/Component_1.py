import numpy as np

def check_SOn(matrix: m, float: epsilon = 0.01) -> bool:
    # Step 1: Check if the matrix is a square.
    if matrix.shape[0] != matrix.shape[1]:
        return False
    
    # Step 2: Check the orthogonality condition.
    # --> m.T * m = I
    identity = np.eye(matrix.shape[0]) # Identity matrix.
    orthogonality_check = np.allclose(np.dot(matrix.T, matrix), identity, atol = epsilon)
    
    # Step 3: Check if the determinant is close to 1.
    determinant_check = np.isclose(np.linalg.det(matrix), 1.0, atol = epsilon)
    
    # Both checks must pass for matrix to bleong to SO(n)
    return orthogonality_check and determinant_check

def check_quaternion(vector: v, float: epsilon = 0.01) -> bool:
    # Step 1: Calculate the norm of the quaternion.
    norm = np.linalg.norm(vector)
    
    # Step 2: Check if the norm is close to 1.
    return np.isclose(norm, 1.0, atol = epsilon)

def check_SEn(matrix: m, float: epsilon = 0.01) -> bool:
    pass