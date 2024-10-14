def max_end3(nums):
    """Returns a new list"""
    output = []
    maxval = max(nums[0], nums[-1])
    for num in nums:
        output.append(maxval)
    return output
#test
print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
