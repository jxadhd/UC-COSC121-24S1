def silly(i, j):
    """Does something silly"""
    if j < i and j > 10 and i != 16:
        return True
    else:
        return False

print(silly(5, 2))