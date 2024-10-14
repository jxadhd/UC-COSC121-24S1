def count_evens(nums):
    """Returns number of even ints in list(nums)"""
    output = int()
    for item in nums:
        if item % 2 == 0:
            output += 1
    return output
#Test
print(count_evens([2, 1, 2, 3, 4]))
