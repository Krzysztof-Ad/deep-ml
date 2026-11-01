import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    A = np.asarray(A, dtype=float)

    if A.shape != (2, 2):
        raise ValueError("A must be a 2x2 matrix")

    a, b = A[0]
    c, d = A[1]

    y1 = c + b
    x1 = a - d
    y2 = c - b
    x2 = a + d

    h1 = np.hypot(x1, y1)
    h2 = np.hypot(x2, y2)

    sing1 = (h1 + h2) / 2
    sing2 = abs(h1 - h2) / 2
    s = np.array([sing1, sing2])

    theta1 = np.arctan2(y1, x1)
    theta2 = np.arctan2(y2, x2)

    alpha = (theta1 + theta2) / 2
    beta = (theta1 - theta2) / 2

    U = np.array([
        [np.cos(alpha), -np.sin(alpha)],
        [np.sin(alpha),  np.cos(alpha)]
    ])

    V = np.array([
        [np.cos(beta), -np.sin(beta)],
        [np.sin(beta),  np.cos(beta)]
    ])

    if h1 > h2:
        V[:, 1] *= -1

    return U, s, V.T
