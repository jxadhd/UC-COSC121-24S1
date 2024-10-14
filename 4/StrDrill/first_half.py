def first_half(s):
    """Returns first half of s"""
    if len(s) % 2 != 0:
        s.replace(s[-1:], '')
    mid = len(s) // 2
    output = s[:mid]
    return output
#Test
print(first_half('WooHoo'))
