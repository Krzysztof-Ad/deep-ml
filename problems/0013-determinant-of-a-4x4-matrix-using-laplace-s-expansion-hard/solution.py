def determinant_nxn(matrix: list[list[int|float]]) -> float:
	n = len(matrix)

	if (n == 1):
		return matrix[0][0]

	det = 0;
	i = 0

	for j in range (n):
		minor = [
			[matrix[r][k] for k in range (n) if k != j]
			for r in range(n) if r != i
		]
		det += (-1) ** (i + j) * matrix[i][j] * determinant_nxn(minor)
	
	return det

def determinant_4x4(matrix: list[list[int|float]]) -> float:
	return determinant_nxn(matrix)



