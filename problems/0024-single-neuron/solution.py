import math

def sigmoid(z: float) -> float:
	return 1 / (1 + math.exp(-z))

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	probabilities = []
	for data in features:
		sm = 0
		for i in range(len(weights)):
			sm += weights[i] * data[i]
		sm += bias
		result = sigmoid(sm)
		probabilities.append(result)
	
	errors = []
	for i in range(len(probabilities)):
		errors.append((probabilities[i] - labels[i]) ** 2)
	
	mseSum = 0
	for error in errors:
		mseSum += error
	
	mse = mseSum / len(errors)

	return probabilities, mse