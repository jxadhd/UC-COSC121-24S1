squares = [0, 22, 1, 4, 9, 16, 25, 35, 49]
var2 = 1
squares.insert(1, var2)
print(squares[:])
print(squares[3:])

items = [0, 3, 7, 5, 1]
item = items.pop(4)
print(item)
print(items)

def nth_item(data, n):
    """DS"""
    return data[n]

item = nth_item([10, 20, 30], 2)
print(item)

a = [81, 82, 83]
b = a
print(a is b)

def duplicate_last(data):
    """DS"""
    data2 = data.copy()
    data2.append(data2[-1])
    return data2

original = [1,2,3]
result = duplicate_last(original)
print(result)

original = [1,2,3]
result = duplicate_last(original)
print('Returned list:', result)
# check that original hasn't changed
print('Original list:', original)

item = duplicate_last(['hi'])
print(item)

number = 2
numbers = [0, 1, 2, 3, 4]
for number in numbers:
    print(number)
print(number)

def concatenate(strings):
    """Docstring"""
    concatenated = ''
    for string in strings:
        concatenated += string
    return concatenated

print(concatenate(["x", "yy", "zzz"]))