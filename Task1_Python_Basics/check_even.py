def get_even_numbers(lst):
    """Finds all even numbers from a list."""
    return [num for num in lst if num % 2 == 0]
print(f"6. Evens in [1, 2, 3, 4, 5]: {get_even_numbers([1, 2, 3, 4, 5])}")
