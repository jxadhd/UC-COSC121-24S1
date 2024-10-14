def upper_case(strings):
    """DS"""
    new = []
    for each in strings:
        new.append(each.upper())
    return new
#Test
data = ['HEY', 'Harry']
print(upper_case(data))