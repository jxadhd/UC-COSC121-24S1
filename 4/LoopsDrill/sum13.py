def sum13(nums):
    """DS if I bothered"""
    skip_next = False
    total = 0
    for num in nums:
        if num == 13:
            skip_next = True
        elif not skip_next:
            total += num
        else:
            skip_next = False
    return total
#test
print(sum13([1, 2, 2, 1, 13]))
print(sum13([13, 2, 2, 1]))
