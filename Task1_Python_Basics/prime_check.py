def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f"5. Is 7 prime?: {is_prime(7)}")
