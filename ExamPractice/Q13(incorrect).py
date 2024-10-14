def guess_mask(word, guess):
    """Returns guess result"""
    word = word.lower()
    guess = guess.lower()
    if len(word) != len(guess):
        return 'ERROR'
    result = ''
    for i in range(len(word)):
        if word[i] == guess[i]:
            result += "Y"
        elif word[i] not in guess:
            result += 'N'
        elif word[i] in guess and word[i] != guess[i]:
            result += '?'
    return result

#Test
mask = guess_mask("camel", "crate")
print(mask)
print(guess_mask('time', 'tyme'))
