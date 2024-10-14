def find_key(input_dict, value):
    """Q17"""
    for key, val in input_dict.items():
        if val == value:
            return key
    return None

# Test the function with your examples
test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'b'))  # Output: 20
print(find_key(test_dictionary, 'e'))  # Output: None