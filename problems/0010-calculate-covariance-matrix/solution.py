def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	n = len(vectors)
	N = len(vectors[0])

	means = [sum(v) / N for v in vectors]

	result = [[0.0] * n for _ in range(n)]

	for i in range (n):
		for j in range(n):
			for k in range (N):
				result[i][j] += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])

			result[i][j] /= (N - 1)

	return result