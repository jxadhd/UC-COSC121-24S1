def double_char(s):
    """Returns str where every char from s appears twice"""
    output = str()
    for char in s:
        output += char * 2
    return output
#Test
print(double_char('The'))
