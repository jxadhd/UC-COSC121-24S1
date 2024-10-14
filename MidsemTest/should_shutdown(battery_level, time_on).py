def should_shutdown(battery_level, time_on):
    """Decides if should_shutdown == True or False"""
    if time_on < 60:
        if battery_level < 4.7:
            return True
        else:
            return False
    elif time_on >= 60:
        if battery_level < 4.8:
            return True
    else:
        return False
    #Test cases
ans = should_shutdown(5, 10)
print(ans)
ans = should_shutdown(4.74, 90)
print(ans)
ans = should_shutdown(4.74, 50)
print(ans)
