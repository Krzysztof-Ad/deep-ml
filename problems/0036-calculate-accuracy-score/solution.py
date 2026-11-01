import numpy as np

def accuracy_score(y_true, y_pred):
	correct = 0
	per = len(y_pred)

	for i in range(per):
		if (y_pred[i] == y_true[i]):
			correct += 1
	
	return correct / per