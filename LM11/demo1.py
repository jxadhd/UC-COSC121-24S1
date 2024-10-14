"""A first simple matplotlib demo"""

import math
import matplotlib.pyplot as plt

NUM_CYCLES = 2  # Number of cycles to plot

def main():
    """Plot a cosine function"""
    axes = plt.axes()
    x_values = range(0, NUM_CYCLES * 360)  # An x-value every degree
    y_values = []
    for x_value in x_values:
        y_value = math.cos(2 * math.pi * x_value / 360)
        y_values.append(y_value)
    axes.plot(x_values, y_values)
    axes.set_title("cos (x)")
    axes.set_xlabel("x (degrees)")
    axes.grid(True)
    plt.show()

main()
