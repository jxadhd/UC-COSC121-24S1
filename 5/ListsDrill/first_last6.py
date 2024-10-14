def first_last6(nums):
    """True if 6 is index 0 or -1 in list(nums)"""
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False
#Test
print(first_last6([1, 2, 6]))
print(first_last6([3, 2, 1]))
