import numpy as np

def to_categorical(x, n_col=None):
	n = n_col

	if n == None:
		n = max(x) + 1

	result = []

	for nr in x:
		current = []
		for i in range (n):
			if i != nr:
				current.append(0.0)
			else:
				current.append(1.0)
		result.append(current)
	
	result = np.array(result)
	
	return result
