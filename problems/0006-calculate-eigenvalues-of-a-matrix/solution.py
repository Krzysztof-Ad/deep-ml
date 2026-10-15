def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]

	tr = a + d
	det = a * d - b * c

	# now we have something like λ^2 - tr * λ + det = 0
	# we solve it with delta

	delta = tr ** 2 - 4 * 1 * det
	sqrt_delta = delta ** 0.5

	eigenvalues = [(tr + sqrt_delta) / 2, (tr - sqrt_delta) / 2]

	return eigenvalues