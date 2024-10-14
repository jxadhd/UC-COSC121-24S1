def divisible_by_8(number):
    """DS here"""
    if number % 8 == 0:
        return True
    else:
        return False
#Test
print(divisible_by_8(16))
print(divisible_by_8(18))
print(divisible_by_8(-40))
