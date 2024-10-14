import numpy as np

def print_rainfall_stats(filename):
    """Prints rainfall stats"""

    data = np.loadtxt(filename, delimiter=',', skiprows=9, usecols=3)

    print(f'{data.shape[0]} records read')
    print(f'Minimum: {data.min():.2f} mm')
    print(f'Maximum: {data.max():.2f} mm')
    print(f'Average: {data.mean():.2f} mm')
    print(f'Standard deviation: {data.std():.2f} mm')

print_rainfall_stats('laketaylorstation2005.txt')
