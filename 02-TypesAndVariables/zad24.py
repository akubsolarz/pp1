nr_rejes = input("podaj numer rejestracji auta: ")

PoOd = nr_rejes[0:2]

print(f" podana rejestracja {nr_rejes}")
if(PoOd == 'KK' or PoOd == 'KR'):
    print("auto jest z krakowa: true")
else:
    print("auto jest z krakowa: false")
