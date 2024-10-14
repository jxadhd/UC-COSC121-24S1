import matplotlib.pyplot as plt

def plot_values(x_values, y_values):
    """Takes a list of x and y values and draws a highly
    basic line graph."""

    axes = plt.axes()
    axes.plot(x_values, y_values)
    axes.grid(True)
    axes.set_title("My Data")
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    plt.show()

    #Test
plot_values([0.0, 0.2, 0.4, 0.6, 0.8, 1.0], [3.2, 7.9, 2.6, 5.1, 4.9, 6.0])