def word_counter(input_str):
    """Returns dictionary of input_str occurence counts"""
    words = input_str.lower().split()
    word_count_dict = {}
    for word in words:
        if word not in word_count_dict:
            word_count_dict[word] = 1
        else:
            word_count_dict[word] += 1
    return word_count_dict
# Test the function with your examples
word_count_dict = word_counter("This is a sentence this is")
print(word_count_dict)  # Output: {'this': 2, 'is': 2, 'a': 1, 'sentence': 1}

word_count_dict = word_counter("A WORD is a word it is")
print(word_count_dict)  # Output: {'a': 2, 'word': 2, 'is': 2, 'it': 1}