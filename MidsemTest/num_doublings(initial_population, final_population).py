def num_doublings(initial_population, final_population):
    """Counts how long for given population increase"""
    days = 0
    while initial_population < final_population:
        initial_population *= 2
        days += 1
    return days
ans = num_doublings(1, 8)
print(ans)