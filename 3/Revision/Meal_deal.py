def meal_deal(spend, is_birthday):
    """Returns discount based on spend and BD"""    
    if spend < 60 and is_birthday == False:
        discount = 0
    elif spend >=60 and spend < 80 and is_birthday == False:
        discount = 5
    elif spend >= 80 and is_birthday == False:
        discount = 20
    elif spend < 55 and is_birthday == True:
        discount = 0
    elif spend >=55 and spend < 75 and is_birthday == True:
        discount = 5
    elif spend >= 75 and is_birthday == True:
        discount = 20
    return discount
print(meal_deal(55, False))