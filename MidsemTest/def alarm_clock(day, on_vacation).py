def alarm_clock(day, on_vacation):
    """DS"""
    if day > 0 and day < 6 and on_vacation == False:
        return "7:00"
    elif day == 0 or day == 6:
        if on_vacation == False:
            return "10:00"
        else:
            return "off"
    elif day > 0 and day < 6 and on_vacation == True:
        return "10:00"
    
print(alarm_clock(0, True))