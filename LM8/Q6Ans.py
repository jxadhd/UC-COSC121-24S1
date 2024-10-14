"""Print all the perfect squares from 2 up to a given maximum.
   This version is refactored to make it more understandable
   and more maintainable."""

import math

def read_bound(prompt):
    """Reads the upper bound from the standard input (keyboard).
       If the user enters something that is not a positive integer
       the function issues an error message and retries
       repeatedly - as per the original code."""
    
    bound = None
    while bound is None:
        line = input(prompt)
        if line.isnumeric():
            bound = int(line)
        else:
            print("You must enter a positive number.")
    return bound


def is_perfect_square(number):
    """Returns True if and only if number is a perfect square, 
    otherwise returns False."""

    root = math.sqrt(number)
    return root == int(root)


def print_squares(lower_bound, upper_bound, squares):
    """Print the given list of all the squares up to the given upper bound.
    The printout should be in the same format as the original code."""

    print(f"The perfect squares from {lower_bound} to {upper_bound} are: ")
    for square in squares:
        print(square, end=" ")
    print()
    

def main():
    """Every home should have one"""
    lower_bound = read_bound("Enter the lower bound: ")
    upper_bound = read_bound("Enter the upper bound: ")
    squares = []
    for number in range(lower_bound, upper_bound + 1):
        if is_perfect_square(number):
            squares.append(number)

    print_squares(lower_bound, upper_bound, squares)

main()
