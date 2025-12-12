def reverse_string(s):
    """Reverses a string without using built-in reverse()."""
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
 print(f"4. Reverse 'Python': {reverse_string('Python')}")
  
