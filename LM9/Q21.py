def generate_dictionary(filename):
    """Generates dictionary of word occurences from file"""
    fileopen = open(filename, 'r')
    data = fileopen.readlines()
    fileopen.close()
    object_dict = {}
    for line in data:
        object_name = line.strip().lower()
        if object_name:
            if object_name not in object_dict:
                object_dict[object_name] = 1
            else:
                object_dict[object_name] += 1
    return object_dict