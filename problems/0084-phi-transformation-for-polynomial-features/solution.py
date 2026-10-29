import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	"""
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""

	result = []
	for number in data:
		expansion = []
		for i in range (degree + 1):
			expansion.append(number ** i)
		result.append(expansion)

	return result