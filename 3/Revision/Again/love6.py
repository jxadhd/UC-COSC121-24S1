def love6(num1, num2):
    """Return True if num1 or num2 == 6 or SUM or DIFF == 6
    """
    if num1 == 6 or num2 == 6:
        return True
    elif num1 + num2 == 6:
        return True
    elif num2 - num1 == 6 or num1 - num2 == 6:
        return True
    else:
        return False
#Test
print(love6(1, 5))
print(love6(6, 4))