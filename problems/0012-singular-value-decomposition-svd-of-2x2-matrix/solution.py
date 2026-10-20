import numpy as np 
def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    B = A.T @ A
    theta = 0.5 * np.arctan2(2 * B[0,1], (B[0,0] - B[1,1]))
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    D = R.T @ B @ R
    eigenvalues = np.diag(D)
    singular_values = np.sqrt(eigenvalues)
    E = np.diag(1 / singular_values)
    V = R
    U = A @ V @ E
    V_T = V.T
    return(U, singular_values, V_T)