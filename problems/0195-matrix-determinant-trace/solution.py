def determinant_nxn(matrix: list[list[float]]) -> float:
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

def trace(matrix: list[list[float]]) -> float:
	sum = 0
	for i in range (len(matrix)):
		sum += matrix[i][i]
	
	return sum

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	
	return (determinant_nxn(matrix), trace(matrix))