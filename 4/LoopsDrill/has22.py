def has22(nums):
    """DS here"""
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
#Test
print(has22([1, 2, 2]))
print(has22([1, 2, 21, 2]))
print(has22([2, 1, 2]))