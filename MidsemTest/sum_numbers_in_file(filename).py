def sum_numbers_in_file(filename):
    """Returns sum of all numbers in file"""
    stuff = open(filename, "r")
    nums = stuff.read()
    lines = nums.splitlines()
    return sum(int(lines) for lines in lines)
filename = "testfile.txt"
print(sum_numbers_in_file(filename))