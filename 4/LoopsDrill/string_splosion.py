def string_splosion(s):
    """Imagine if I bothered to write docstrings"""
    output = str()
    for i in range(len(s)):
        output += s[:i+1]
    return output

#Test
print(string_splosion('Code'))
