def love6(num1, num2):
    """Docstring"""
    if num1 == 6 or num2 == 6:
        return True
    elif (num1 + num2) == 6:
        return True
    elif (num1 - num2) == 6 or (num2 - num1) == 6:
        return True
    else:
        return False
"""Test code below"""
print(love6(4, 11))