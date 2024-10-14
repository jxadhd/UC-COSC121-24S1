def set_lowercase(strings):
    """Modifies list by replacing string with lowercase"""
    for i in strings:
        strings[i] = strings.lower()
words = ['Right', 'SAID', 'Fred']
set_lowercase(words)
print(words)