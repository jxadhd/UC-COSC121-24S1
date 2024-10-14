def char_freqs(input_str):
    """Returns a dictionary mapping characters and each occurence count"""
    output = {}
    for char in input_str:
        if char in output:
            output[char] += 1
        else:
            output[char] = 1
    return output
#Test
count_dict = char_freqs("aaAA BbBb cC Dd ee f")
for char, count in sorted(count_dict.items()):
    print(repr(char),'->', count)