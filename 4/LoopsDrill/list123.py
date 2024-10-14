def list123(nums):
    """Returns True if 1, 2 ,3 appears in list(nums)"""
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] and nums[i + 2] == 3:
            return True
    return False
# Test cases
print(list123([1, 2, 3]))  # Output: True
print(list123([1, 2, 4, 3]))  # Output: False
print(list123([1, 2, 3, 4, 5]))  # Output: True
print(list123([5, 1, 2, 3, 6]))  # Output: True
print(list123([1, 1, 2, 3, 1]))