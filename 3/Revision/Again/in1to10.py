def in1to10(n, outside_mode):
    """Returns T or F"""
    if outside_mode:
        if n <= 1 or n >= 10:
            return True
        else:
            return False
    else:
        if n >= 1 and n <= 10:
            return True
        else:
            return False
#Test
print(in1to10(5, False))
print(in1to10(11, True))
print(in1to10(11, False))