def flawed_merge(list_1, list_2):
    """Returns all elements of list_1 except last, all elements of list_2 except
    first"""
    return list_1[:-1] + list_2[1:]
