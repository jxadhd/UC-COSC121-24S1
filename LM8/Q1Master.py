"""Prints total cost of items"""

def main():
    """Compute and print the total cost of a number of items"""

    # First initialise all variables
    cost_per_item = 27      # Without discount
    discount_percent = 10
    discount_threshold = 20

    # Get the number of items to be priced.
    n_items = int(input("Number of items? "))

    # Now compute the total cost
    cost = n_items * cost_per_item                  # line 1
    if n_items > discount_threshold:                # line 2
        cost = cost * (1 - discount_percent / 100)  # line 3

    # Print the results
    print(f'{n_items} items cost ${cost:.2f}')

main()
