def print_numbered_lines(filename):
    """Prints lines in file with line #:"""
    with open(filename, "r") as file:
        for i, line in enumerate(file, start=1):
            print(f"{i}: {line.rstrip()}")
print_numbered_lines('testfile.txt')