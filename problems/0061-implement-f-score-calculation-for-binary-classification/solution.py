import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	
	TP = ((y_true == 1) & (y_pred == 1)).sum()

	rc = (y_true == 1).sum()
	pc = (y_pred == 1).sum()

	recall = TP / rc
	precision = TP / pc

	result = (1 + beta ** 2) * (precision * recall) / (beta ** 2 * precision + recall)

	return round(result, 3)