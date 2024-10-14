def little_sum(number_list, limit):
    """DS goes here normally"""
    output = 0
    for num in number_list:
        if num < limit:
            output += num
    return output
#Test
total = little_sum([1, 2, 3, 4, 5, 6], 3)
print(total)
total = little_sum([6, 3, 4, 1, 5, 2], 4)
print(total)