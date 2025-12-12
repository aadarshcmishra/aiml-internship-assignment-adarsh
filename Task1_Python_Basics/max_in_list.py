def find_max(lst):
    """Finds maximum element in a list."""
    if not lst: return None
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum
