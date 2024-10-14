import math
import numpy as np
import matplotlib.pyplot as plt

def generate_x_values(start, end, num_values):
    """Returns list(output) of num_values(range(start, end)) inclusive"""
    step = (end - start) / (num_values - 1)
    output = []
    for num in range(num_values):
        x = start + num * step
        output.append(x)
    return output

def main():
    """Plot out generate_x_values(-4.0, 4.0, 400)"""
    x_values = generate_x_values(-4.0, 4.0, 400)
    y_values = [(1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2) for x in x_values]
    axes = plt.axes()
    axes.plot(x_values, y_values)
    axes.grid(True)
    axes.set_title("A normal distribution, f(x), with mean = 0, variance = 1")
    axes.set_xlabel("x")
    axes.set_ylabel("f(x)")
    plt.show()

main()