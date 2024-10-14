nums = [9, 3, 8, 11, 5, 29, 2]
best_num = 0
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

def my_max(data):
    """Doc"""
    
    result = float('-inf')
    for nums in data:
        if nums > result:
            result = nums
    return result

#Test code
print(my_max([11, 99, 3, -6]))
print(my_max([-3, -5, -9, -10]))

def cubes(data):
    """Data is a list"""
    result = []
    for num in data:
        result.append(num ** 3)
    return result
    
cubes_list = cubes([1, 2, 4])
print(cubes_list)

cubes_list = cubes([5])
print(cubes_list)

# Step 1
words = 'This is a SENTENCE'.split()

#Step 2
lower_case_words = []

#Step 3
for word in words:
    word = word.lower()  # Convert to lower case
    lower_case_words.append(word)

#Step 4
lower_case_words.sort()

#Step 5
alphabetical = 'In alphabetical order:'
for word in lower_case_words:
    alphabetical += ' ' + word

#Step 6
print(alphabetical)

def absolute_nums(numbers):
    """DS"""
    nums = [abs(nums) for nums in numbers]
    return nums

print(absolute_nums([2, -3, -7]))

def lower_case(strings):
    """DS"""
    strlist = [str.lower(val) for val in strings]
    return strlist

words = ['HEY', 'Harry']
print(lower_case(words))

def evens(numbers):
    """DS"""
    result = []
    for stevens in numbers:
        if stevens % 2 == 0:
            result.append(stevens)
    return result

print(evens([1, 2, 3, 4, 5, 6, 10, 11]))

def long_enough(strings, min_length):
    """DS"""
    output = []
    for strvar in strings:
        if min_length <= len(strvar):
            output.append(strvar)
    return output

list_of_strings = ['a', 'bc', 'def', 'ghij', 'klmno']
print(long_enough(list_of_strings, 3))

string = 'stuff'
print(string[2]) 

def top_and_tail(string):
    """DS"""
    result = string[1:-1]
    return result

print(top_and_tail('stubby'))
print(top_and_tail('another test string'))

def vertical_strings(string):
    """DS"""
    for char in string:
        print(char * len(string))

# Example usage:
vertical_strings("hello")

def are_anagrams(word1, word2):
    """A function are_anagrams(word1, word2) which returns True if the two
    paremeters are anagrams"""
    if word1 == word2:
        return False
    return sorted(word1) == sorted(word2)

# Example usage:
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False

location = (123, 'Fake St', 4567)
number, street, post_code = location         
print("Number: " + str(number))
print("Street: " + street)
print("Post code: " + str(post_code))

def dangerous(a):
    z = 4064427
    x = z + a
    return a // x
print(dangerous(-4064427))