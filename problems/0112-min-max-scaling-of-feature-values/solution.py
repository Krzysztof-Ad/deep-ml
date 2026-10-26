def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    
    result = []
    mn = min(x)
    mx = max(x)

    for el in x:
        result.append((el - mn) / (mx - mn))
    
    return result