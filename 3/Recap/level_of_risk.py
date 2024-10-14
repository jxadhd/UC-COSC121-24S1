def level_of_risk(speed, temperature):
    """DS goes here"""
    if temperature <= 64:
        if speed < 61:
            return 3
        elif speed >= 61:
            return 6
    elif temperature > 64:
        if speed < 61:
            return 5
        elif speed >= 61:
            return 8
#Test
print(level_of_risk(60, 62))
print(level_of_risk(66, 64))
