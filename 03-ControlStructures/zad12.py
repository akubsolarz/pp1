imie1 = input("podaj pierwsze imie: ")
wiek1 = int(input("podaj pierwszy wiek: "))

imie2 = input("podaj drugie imie: ")
wiek2 = int(input("podaj drugi wiek: "))

print(f"Enter first person name:  {imie1} \n Enter first person age: {wiek1} \n Enter second person name: {imie2} Enter second person age: {wiek2}")

if(wiek1 >= 18 and wiek2 >= 18):
    print(f" Both {imie1} and {imie2} are adults")
else:
    print(f" Both {imie1} and {imie2} are not adults")