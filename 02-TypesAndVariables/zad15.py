#pobiera dane z klawiatury (temperature w celcjuszach)
tcel = input("podaj temperature w celcjuszach ")

#przeliczanie za celcjusza na kelvina
kelv = int(tcel)+ 273.15

#przeliczanie za celcjusza na farenchajta
fare = (int(tcel) *1.8)+32

#wypisuje nasze wyniki
print(f" temperatura przeliczona na kelviny: {kelv} \n temperatura przeliczona na farenchajta: {fare}")

