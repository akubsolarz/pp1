wiek = int(input("podaj wiek: "))

print(f"Enter the dog's age in human years: {wiek} ")
if wiek >= 2 :
    print(f"The dog's age in dog’s years is {21+(wiek-2)*4} years.")
else:
    print(f"The dog's age in dog’s years is {wiek*10.5} years.")
