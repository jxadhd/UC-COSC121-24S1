def max_num_in_file(filename):
    """Returns largest integer in a file"""
    with open(filename, 'r') as file:
        return max(int(line) for line in file)
