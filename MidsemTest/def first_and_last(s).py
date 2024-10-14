def first_and_last(s):
    """Returns empty str if s is empty, otherwise first and last char of s"""
    outputifnil = str()
    if len(s) >= 1:
        return s[0] + s[-1]
    else:
        return outputifnil

print(first_and_last("s"))