def remove_duplicates(lst):
    """Removes duplicates from a list without using set()."""
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
