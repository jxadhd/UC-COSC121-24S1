"""LM11 Q1!"""

import matplotlib.pyplot as plotter

def plot_values(x_values, y_values):
    """If I knew what MatPlotLib did, I would put it in this docstring"""
    axes = plotter.axes()
    axes.plot(x_values, y_values)
    axes.grid(True)
    plotter.show()
#Test
plot_values([0.0, 0.2, 0.4, 0.6, 0.8, 1.0], [3.2, 7.9, 2.6, 5.1, 4.9, 6.0])
