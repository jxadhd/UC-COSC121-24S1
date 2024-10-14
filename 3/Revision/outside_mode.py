def in1to10(n, outside_mode):
    """..."""
    if  n >= 1 and n <= 10 and not outside_mode == True:
        return True
    elif n <= 1 or n >= 10 and not outside_mode == False:
        return True
    else:
        return False
"""test code below"""
print(in1to10(5, False))
print(in1to10(11, True))
print(in1to10(11, False))