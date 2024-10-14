def generate_x_values(start, end, num_values):
    """Returns list(output) of num_values(range(start, end)) inclusive"""
    step = (end - start) / (num_values - 1)
    output = []
    for num in range(num_values):
        x = start + num * step
        output.append(x)
    return output

#Test
values = generate_x_values(1, 2, 3)
print(values)

x_values = generate_x_values(-4.0, 4.0, 400)
print(f"Number of values: {len(x_values)}")
print(f"First three: {x_values[0]:.4f}, {x_values[1]:.4f}, {x_values[2]:.4f}")
print(f"Final three: {x_values[-3]:.4f}, {x_values[-2]:.4f}, {x_values[-1]:.4f}")