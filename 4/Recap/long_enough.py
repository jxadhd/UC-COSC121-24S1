def long_enough(strings, min_length):
    """Returns a list from list(strings) with a length greater than int(min_length)."""
    accepted = []
    for word in strings:
        if len(word) >= min_length:
            accepted.append(word)
    return accepted
strings = ['a', 'bc', 'def', 'ghij', 'klmno']
print(long_enough(strings, 3))