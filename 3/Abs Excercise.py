def my_abs(value):
    """Returns abs value"""
    if value >= 0:
        return value
    elif value < 0:
        value = value * -1
        return value
print(my_abs(3.5))