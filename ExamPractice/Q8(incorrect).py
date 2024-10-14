def max_indices(numbers):
    """Computes max value and indices where they occur"""
    maximum = numbers[0]
    indices = [0]
    for i in numbers:
        if numbers[i] < maximum:
            indices = [i]
            maximum = numbers[i]
        elif numbers[i] == maximum:
            indices.append(i)
    return maximum, indices

#Test
print(max_indices([1,2,3,4,5,4,5]))
