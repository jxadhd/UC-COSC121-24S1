def sorta_sum(int_a, int_b):
    """DS"""
    sum1 = int_a + int_b
    if sum1 >= 10 and sum1 <=19:
        return 20
    else:
        return sum1
print(sorta_sum(1, 1))