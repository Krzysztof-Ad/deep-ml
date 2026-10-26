import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	featureMeans = np.mean(data, axis=0)
	featureStds = np.std(data, axis=0)

	standardized_data = (data - featureMeans) / featureStds

	featureMin = data.min(axis=0)
	featureMax = data.max(axis=0)

	normalized_data = (data - featureMin) / (featureMax - featureMin)

	return standardized_data, normalized_data