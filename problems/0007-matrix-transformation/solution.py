import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	det_T = np.linalg.det(T)
	det_S = np.linalg.det(S)

	if (det_S == 0 or det_T == 0):
		return -1
	
	inv_T = np.linalg.inv(np.array(T)).tolist()

	transformed_matrix = (np.array(inv_T) @ np.array(A) @ np.array(S)).tolist()

	return transformed_matrix