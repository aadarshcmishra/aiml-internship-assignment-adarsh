def is_palindrome(data):
    """Checks if a string or number is a palindrome."""
    s = str(data)
    return s == s[::-1]
