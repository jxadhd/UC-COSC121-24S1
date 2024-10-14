def file_size(filename):
    """Returns number of characters in given file"""
    file = open(filename, "r")
    contents = file.read()
    file.close()
    return len(contents)
#Test Case
print(file_size("testfile.txt"))
