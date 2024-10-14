def has23(nums):
    """Returns True if list(nums) contains a 2 or 3"""
    for num in nums:
        if num == 2 or num == 3:
            return True
    return False
#test
print(has23([2, 5]))
print(has23([42, 53]))
print(has23([4, 3]))
