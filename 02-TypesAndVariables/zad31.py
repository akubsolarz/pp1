import random

kostka =  random.randint(1,6)

ges = int(input("zgadnij numer: "))

print(f" zgadłeś: {kostka == ges}")