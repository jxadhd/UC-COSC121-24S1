"""none"""
def concat_short_words(s):
    """Returns a concatenation of all the words in s that are at most
        4 characters in length.
    """
    words = s.split()
    result = ''
    i = 0
    while i < len(words):
        if len(words[i]) <= 4:
            result = result + words[i]
        i += 1
    return result
test_string = 'This is a short sentence, ok?'
print(concat_short_words(test_string))
