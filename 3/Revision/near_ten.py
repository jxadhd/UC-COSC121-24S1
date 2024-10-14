def near_ten(num):
    """DS"""
    remainder = num % 10
    return remainder <= 2 or remainder >= 8

# Example usage:
print(near_ten(12))  # True
print(near_ten(17))  # False
print(near_ten(18))  # True
