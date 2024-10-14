"""Matplotlib/numpy revisions Q12"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    """Runs graph"""
    x_values = np.linspace(-10.0, 10.0, 100)
    y_values = x_values ** 3 - 3 * x_values + 250
    
    axes = plt.axes()
    axes.plot(x_values, y_values)
    axes.grid(True)
    axes.set_title("$y = x^3 - 3x + 250$")
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    plt.show()

main()