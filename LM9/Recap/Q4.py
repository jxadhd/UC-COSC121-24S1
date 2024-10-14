def inverted_word_counts(word_count_dict):
    """Returns inverted version of input"""
    inverted = {}
    for word, count in word_count_dict.items():
        if count not in inverted:
            inverted[count] = []
        inverted[count].append(word)
    for count in inverted:
        inverted[count].sort()
    return inverted
#Test
test_dict = {'a': 20, 'blotto': 1, 'bingo':1, 'x': 5}
inverse = inverted_word_counts(test_dict)
for count in sorted(inverse.keys()):
    print('{}: {}'.format(count, inverse[count]))