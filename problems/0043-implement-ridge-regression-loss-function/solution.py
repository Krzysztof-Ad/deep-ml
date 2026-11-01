import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	n = len(y_true)
	d = len(w)

	fsm = 0
	r = X @ w
	for i in range(n):
		fsm += (y_true[i] - r[i]) ** 2
	
	fsm /= n

	ssm = 0
	for i in range (d):
		ssm += w[i] ** 2
	
	ssm *= alpha

	loss = fsm  + ssm

	return loss