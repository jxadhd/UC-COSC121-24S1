""" np.loadtxt and matplotlib to extract and plot all the rainfalls from
    the file laketaylorstation2005.txt.
    """
import numpy as np
import matplotlib.pyplot as plt

def load_rainfall_data(filename):
    """Load rainfall data"""
    data = np.loadtxt(filename, delimiter=',', skiprows=9, usecols=3)
    return data

def plot_rainfall(days, data):
    """Plotter function"""
    axes = plt.axes()
    axes.plot(days, data, label='Rainfall')
    axes.set_xlabel('Day number')
    axes.set_ylabel('Rainfall (mm)')
    axes.set_title('Lake Taylor Station Rainfalls, 2005')
    axes.grid(True)
    plt.show()

def main():
    """Main function"""
    filename = 'laketaylorstation2005.txt'
    days = np.arange(1, 366)
    data = load_rainfall_data(filename)
    plot_rainfall(days, data)

main()