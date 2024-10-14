def make_ends(nums):
    """Returns new list containing nums[0] and [-1]"""
    return [nums[0], nums[-1]]
print(make_ends([1, 2, 3]))
print(make_ends([7, 4, 6, 2]))
