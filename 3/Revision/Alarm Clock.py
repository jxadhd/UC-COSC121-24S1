def alarm_clock(day, on_vacation):
    """Alarm goes off at 7:00 work days, and not on weekends, unless on vacation
    then it goes off at 10:00 weekdays only"""
    if on_vacation == False and day >= 1 and day <= 5:
        alarm = "7:00"
    elif on_vacation == False and (day == 6 or day == 0):
        alarm = "10:00"
    elif on_vacation == True and (day >= 1 and day <= 5):
        alarm = "10:00"
    else:
        alarm = "off"
    return alarm
print(alarm_clock(0, True))