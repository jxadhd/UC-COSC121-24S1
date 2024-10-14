"""ModuleDS"""

def generate_x_values(start, end, num_values=[]):
    """FuncDS"""
    delta = (end - start) / (num_values - 1)
    values = [start + i * delta for i in range(num_values)]
    return values
#Test code
print(generate_x_values(1, 2, 3))
x_values = generate_x_values(-4.0, 4.0, 400)
print(f"Number of values: {len(x_values)}")
print(f"First three: {x_values[0]:.4f}, {x_values[1]:.4f}, {x_values[2]:.4f}")
print(f"Final three: {x_values[-3]:.4f}, {x_values[-2]:.4f}, {x_values[-1]:.4f}")