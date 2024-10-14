def are_anagrams(word1, word2):
    """"DS"""
    word1 = word1.lower()
    word2 = word2.lower()
    if word1 == word2:
        return False

    letters1=list(word1)
    letters2=list(word2)
    letters1.sort()
    letters2.sort()

    return letters1 == letters2
#Test
print(are_anagrams("looped", "poodle"))
print(are_anagrams("lopped", "poodle"))
