import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	if (len(a) * len(a[0]) != new_shape[0] * new_shape[1]):
		return []

	reshaped_matrix = [[0] * new_shape[1] for _ in range (new_shape[0])]

	flat = [el for row in a for el in row]

	k = 0
	for i in range (new_shape[0]):
		for j in range (new_shape[1]):
			reshaped_matrix[i][j] = flat[k]
			k += 1

	return reshaped_matrix