import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros(len(b))

	for k in range (n):
		x_new = np.zeros(len(b))

		for i in range (len(x)):

			ssum = 0;

			for j in range (len(A)):
				if (i != j):
					ssum += A[i][j] * x[j]

			x_new[i] = (b[i] - ssum) / A[i][i]
		
		x = x_new
	return x