import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	scores = np.array(scores)

	mx = max(scores)

	sm = 0
	for score in scores:
		sm += np.exp(score - mx)
	
	sm = np.log(sm)
	
	return scores - mx - sm