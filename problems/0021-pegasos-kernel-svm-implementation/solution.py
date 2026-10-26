import numpy as np

def pegasos_kernel_svm(data: np.ndarray, labels: np.ndarray, kernel='linear', lambda_val=0.01, iterations=100, sigma=1.0) -> tuple:
    """
    Train a kernel SVM using the deterministic Pegasos algorithm.
    
    Args:
        data: Training data of shape (n_samples, n_features)
        labels: Labels of shape (n_samples,) with values in {-1, 1}
        kernel: 'linear' or 'rbf'
        lambda_val: Regularization parameter
        iterations: Number of training iterations
        sigma: RBF kernel bandwidth (only used if kernel='rbf')
    
    Returns:
        Tuple of (alphas, bias) where alphas is a list and bias is a float
    """
    if (kernel == 'linear'):
        K = lambda x, z: np.dot(x, z)
    elif (kernel == 'rbf'):
        K = lambda x, z: np.exp(-np.linalg.norm(x - z) ** 2 / (2 * sigma ** 2))
    else:
        raise ValueError("unknown kernel type")

    alpha = np.zeros(data.shape[0])
    b = 0.0

    g = np.zeros(data.shape[0])
    for t in range (1, iterations + 1):
        nt = 1 / (lambda_val * t)

        for i in range (data.shape[0]):
            g = b
            for j in range(data.shape[0]):
                g += alpha[j] * labels[j] * K(data[j], data[i])
            
            if (labels[i] * g < 1):
                alpha[i] += nt * (1 - lambda_val * alpha[i])
                b += nt * labels[i]
            else:
                alpha[i] -= nt * lambda_val * alpha[i]

    return (alpha, b)