def squirrel_play(temp, is_summer):
    """DS"""
    if is_summer == False and temp >= 60 and temp <= 90:
        return True
    elif is_summer == True and temp >= 60 and temp <=100:
        return True
    else:
        return False
print(squirrel_play(55, False))