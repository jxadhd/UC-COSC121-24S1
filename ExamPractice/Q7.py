def string_list(values):
    """Converts list of floats to str"""
    output = []
    for value in values:
        form = f'{value:.2f}'
        output.append(form)
    return output

#Test
numbers = [2.4576, -4.5682, 1.3248, 3/22]
for value in string_list(numbers):
    print(value)