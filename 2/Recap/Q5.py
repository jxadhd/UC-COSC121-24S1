def get_and_print_rect():
    """Asks user for inputs of h and w"""
    wide = float(input("Width of rectangle? "))
    heigh = float(input("Height of rectangle? "))
    area = wide * heigh
    print(f"Area: {area:.2f}")
get_and_print_rect()