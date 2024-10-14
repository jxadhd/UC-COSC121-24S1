""" LM11 Q16
    Identical to Q4 but uses Numpy instead of lists
    """

import math
import matplotlib.pyplot as plt
import numpy as np

def generate_x_values(start, end, num_values=[]):
    """FuncDS"""
    delta = (end - start) / (num_values - 1)
    values = np.linspace(start, end, num_values)
    return values

def normdist(x):
    """FuncDS"""
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)

def main():
    """Plot the graph"""
    x_values = generate_x_values(-4, 4, 400)
    y_values = normdist(x_values)
    axes = plt.axes()
    axes.plot(x_values, y_values)
    axes.set_xlabel('x')
    axes.set_ylabel('f(x)')
    axes.grid(True)
    axes.set_title('A normal distribution, f(x), with mean = 0, variance = 1')
    plt.show()

main()
