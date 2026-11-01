import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    tp = 0
    fn = 0

    for i in range (len(y_pred)):
        if y_true[i] == 1:
            if y_pred[i] == 1:
                tp += 1
            elif y_pred[i] == 0:
                fn += 1
    
    return tp / (fn + tp) if (fn + tp) != 0 else 0