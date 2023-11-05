num1 = int(input("podaj pierwszy numer: "))
num2 = int(input("podaj drugi numer: "))

print(f"Enter number 1: {num1} Enter number 2: {num2}")

if(num1 > 0 or num2 > 0 ):
    print(f"At least one of entered numbers {num1} and {num2} is not negative")
else: 
    print(f"numbers {num1} and {num2} are negative")