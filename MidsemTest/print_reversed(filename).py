def print_reversed(filename):
    """Prints file lines in reverse order"""
    stuff = open(filename, 'r')
    lines = stuff.readlines()
    reversedlines = reversed(lines)
    for line in reversedlines:
        print(line.rstrip())
filename = "testfile.txt"
print_reversed(filename)