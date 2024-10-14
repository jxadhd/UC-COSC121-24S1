def squirrel_play(temp, is_summer):
    """
        Do the squirrels play???
    """
    if is_summer and temp >= 60 and temp <= 100:
        return True
    elif not is_summer and temp >= 60 and temp <= 90:
        return True
    else:
        return False
print(squirrel_play(70, False))
print(squirrel_play(95, False))
