def print_section(size):
    """Prints a wedge of asterisks of a given size"""
    #Assumes size > 0
    for i in range(size, 0, -1):
        print('*' * i)

print_section(8)