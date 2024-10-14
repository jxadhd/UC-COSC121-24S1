def namer(phonebook, phone_number):
    """Returns name in phonebook from given phone_number"""
    for name, number in phonebook.items():
        if number == phone_number:
            return name
    return None
#Test
phonebook = {'Fred':311567, 'Barb':311569, 'josh':556774, 'Bob':556773}
print(namer(phonebook, 556774))