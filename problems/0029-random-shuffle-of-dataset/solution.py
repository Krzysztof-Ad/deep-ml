import numpy as np

def shuffle_data(X, y, seed=None):
	if (seed):
		np.random.seed(seed)
	
	n = X.shape[0]
	
	ids = np.arange(n)
	np.random.shuffle(ids)

	X_res = []
	y_res = []

	for i in range (n):
		X_res.append(X[ids[i]])
		y_res.append(y[ids[i]])

	return (X_res, y_res)