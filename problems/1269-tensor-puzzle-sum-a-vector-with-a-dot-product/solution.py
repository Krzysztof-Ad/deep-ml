import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    n = len(a)

    ones = np.ones(n)

    return a @ ones