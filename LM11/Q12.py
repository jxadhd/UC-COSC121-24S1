"""LM11 Q12"""

import matplotlib.pyplot as plt
import numpy as np

def func(x):
    """Computes values for y"""
    return x ** 3 - 3 * x + 250

def main():
    """main"""
    xvals = np.linspace(-10, 10, 100)
    yvals = func(xvals)
    axes = plt.axes()
    axes.plot(xvals, yvals)
    axes.set_title('$y = x^3 - 3x + 250$')
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.grid('True')
    plt.show()

main()