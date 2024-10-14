def generation(temp, cloud_cover, time):
    """Returns str regarding total solar generation capability"""
    if temp <= 5:
        return 'low'
    elif temp > 5 and cloud_cover > 50:
        if time < 9 or time > 16:
            return 'low'
        else:
            return 'medium'
    elif temp > 5 and cloud_cover <= 50:
        if time < 9:
            return 'medium'
        if time > 16:
            return 'low'
        else:
            return 'high'

#Test
print(generation(10, 45, 10))
print(generation(10, 45, 18))
print(generation(10, 25, 8))
