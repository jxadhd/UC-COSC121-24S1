def print_nth_item_divided(data, n, divisor):
    """prints the nth item of the list data and divides by divisor"""
    try:
        print(data[n] / divisor)
    except IndexError:
        print("Invalid position provided.")
    except TypeError:
        print("Parameters must be numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

print_nth_item_divided([2, 4, 5], 2, 2)
print_nth_item_divided([2, 4, 5], 9, 2)
print_nth_item_divided([2, 4, 5], '1', 2)
print_nth_item_divided([2, 4, 5], 1, 0)
