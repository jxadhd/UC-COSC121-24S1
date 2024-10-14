def max_num_in_file(filename):
    """Returns max num in file"""
    stuff = open(filename, "r")
    nums = stuff.read()
    lines = nums.splitlines()
    return max(int(lines) for lines in lines)
file = "testfile.txt"
print(max_num_in_file(file))
