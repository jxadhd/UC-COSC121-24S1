def sorta_sum(int_a, int_b):
    """Returns sum of a and b, except where SUM = 10-19, then return 20
    """
    if int_a + int_b < 10 or int_a + int_b > 19:
        return int_a + int_b
    else:
        return 20
#Test
print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
