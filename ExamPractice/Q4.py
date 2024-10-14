def generation(solar):
    """Returns rating of solar generation"""
    if solar > 15:
        return 'excellent'
    elif solar < 4:
        return 'poor'
    else:
        return 'average'

print(generation(24))
print(generation(10))
print(generation(1))
