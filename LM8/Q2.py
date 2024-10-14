"""Learning Module Question 2"""

def fun_function(n_items, cost_per_item, discount_percent, discount_threshold):
    """_summary_
    Returns total cost
    """
    cost = n_items * cost_per_item                  # line 1
    if n_items > discount_threshold:                # line 2
        cost = cost * (1 - discount_percent / 100)  # line 3
    return cost

def main():
    """Compute and print the total cost of a number of items"""

    # First initialise all variables
    cost_per_item = 27      # Without discount
    discount_percent = 10
    discount_threshold = 20

    # Get the number of items to be priced.
    n_items = int(input("Count of items? "))

    # Now compute the total cost
    var1 = fun_function(n_items, cost_per_item, discount_percent, discount_threshold)

    # Print the results
    print(f'{n_items} items cost ${var1:.2f}')

main()
