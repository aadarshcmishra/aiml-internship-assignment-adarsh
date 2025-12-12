def dict_squares(numbers):
    """Returns dictionary where key=number and value=square."""
    return {num: num**2 for num in numbers}
print(f"9. Squares [2, 3, 4]: {dict_squares([2, 3, 4])}")
