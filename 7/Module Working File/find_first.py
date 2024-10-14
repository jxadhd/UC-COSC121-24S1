def find_first(value, data, start_index=0):
    """Return the index of the first occurrence of item in data (starting at start_index)
       or -1 if not found.
    """
    index = -1
    for i in range(0, len(data)):
        if value == data[i] and index == -1:
            index = i
    return index

print(find_first(1, [1, 2, 3, 0], ))