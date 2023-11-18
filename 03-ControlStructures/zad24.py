cena1 = int(input("Current product price: "))
cena2 = int(input("Previous product price: "))

proc = 100-((100 * cena2)/cena1)

if proc >= 10:
    print(f"Buy the product!! \nProduct price reduced by {int(proc)}%")