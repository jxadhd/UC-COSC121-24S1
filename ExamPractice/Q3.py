def translator(word):
    """Returns int 0-3 according to Q3 prescription"""
    if word.lower() == 'wacky':
        return 1
    elif word.lower() == 'woolley':
        return 2
    elif word.lower() == 'world':
        return 3
    else:
        return 0

#Test
print(translator('wacky'))
print(translator('Wacky'))
print(translator('WaCky'))
print(translator('WACKY'))