substance = input("What substance would you like to check? ")
ph = float(input("Enter the measured ph: "))
if ph < 7.0:
    print(substance + " is acidic")
elif ph > 7.0:
    print(substance + " is non-acidic/alkali/basic")
else:
    print(substance + " is neutral")
    
quest2 = input("Would you like to test another substance? Y/N ")
if quest2 == "Y":
    print("TBD")
elif quest2 == "N":
    print("TBA")
    
