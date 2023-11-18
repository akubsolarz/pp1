pin =''
tim = 0
while pin != '0805':
    pin = input("Enter the PIN code: ")
    if pin != '0805':
        print("Incorrect...")
        tim += 1
    if tim >= 3:
        print("Sorry, your payment card has been blocked.")
        break