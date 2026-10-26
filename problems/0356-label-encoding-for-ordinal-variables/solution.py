def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """

    result = []

    for value in values:
        idx = -1
        try:
            idx = order.index(value)
        except ValueError:
            idx = -1
        result.append(idx)

    return result