import numpy as np
def precision(y_true, y_pred):
	tp = 0
	fp = 0
	for i in range (len(y_true)):
		if y_true[i] == 0 and y_pred[i] == 1:
			fp += 1
		if y_true[i] == 1 and y_pred[i] == 1:
			tp += 1
	
	return tp / (fp + tp) if (fp + tp) != 0 else 0