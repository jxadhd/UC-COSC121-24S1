"""Print all the perfect squares from 2 up to a given maximum.
   This version is refactored to make it more understandable
   and more maintainable."""
import math

def read_upper_bound():
    """Reads the upper bound from the standard input (keyboard).
       If the user enters something that is not a positive integer
       the function issues an error message and retries
       repeatedly - as per the original code."""
    
    upper_bound = None
    while upper_bound is None:
        line = input("Enter the upper bound: ")
        if line.isnumeric():
            upper_bound = int(line)
        else:
            print("You must enter a positive number.")
    return upper_bound


def is_perfect_square(number):
    """Returns True if and only if number is a perfect square, 
    otherwise returns False."""
    root = math.sqrt(number)
    return root == int(root)


def print_squares(upper_bound, squares):
    """Print the given list of all the squares up to the given upper bound.
    The printout should be in the same format as the original code."""
    
    print(f"The perfect squares up to {upper_bound} are: ")
    for square in squares:
        print(square, end=" ")
    print()
    

def main():
    """Every home should have one"""
    upper_bound = read_upper_bound()
    squares = []
    for num in range(2, upper_bound + 1):
        if is_perfect_square(num):
            squares.append(num)
    
    print_squares(upper_bound, squares)


main()