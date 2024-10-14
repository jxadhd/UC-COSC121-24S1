def first_two(s):
    """DS goes here"""
    return s[:2] if len(s) >= 2 else s
#Test
print(first_two('Hello'))
print(first_two('X'))
