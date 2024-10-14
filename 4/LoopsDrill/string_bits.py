def string_bits(s):
    """Returns new string of every second char, starting with the first.
    """
    return s[0::2]
#Test
print(string_bits('Hello'))
print(string_bits('Hi'))
