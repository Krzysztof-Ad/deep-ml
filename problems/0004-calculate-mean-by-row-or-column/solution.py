def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == 'row':
		means = []
		for row in matrix:
			means.append(sum(row) / len(row))
	elif mode == 'column':
		means = []
		for j in range (len(matrix[0])):
			column_sum = 0
			for i in range (len(matrix)):
				column_sum += matrix[i][j]
			means.append(column_sum / len(matrix))
	else:
		print("ERROR. Wrong mode!")

	return means