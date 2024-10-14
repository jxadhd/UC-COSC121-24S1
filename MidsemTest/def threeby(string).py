"""None"""

def threeby(string):
    """returns a string where every 3rd character in the original string appears
    5 times"""
    result = ''
    for i, char in enumerate(string):
        if (i % 3) == 0:
            result += char * 5
        else:
            result += char
    return result