def odd_numbers(data):
    """returns a new list containing only the elements of data that are odd"""
    newlist = []
    for nums in data:
        if nums % 2 != 0:
            newlist.append(nums)
    return newlist

odds = odd_numbers([22, 11, 33, 44, 55])
print(odds)