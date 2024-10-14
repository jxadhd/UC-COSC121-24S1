def combo_string(str1, str2):
    """DS here"""
    if len(str1) > len(str2):
        short_str = str2
        long_str = str1
    else:
        short_str = str1
        long_str = str2
    return short_str + long_str + short_str

print(combo_string('Hello', 'hi'))
print(combo_string('Z', 'Apple'))
