num = float(input("podaj cene: "))
pro = int(input("podaj zniżke: "))

cena = num * (pro / 100)
zni = num - cena

print(f" Enter price: {num} \n Enter discount %: {pro} \n Reduction: {round(zni,2)} \n Price with discount: {round(cena,2)} " )