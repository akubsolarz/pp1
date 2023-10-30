a = int(input("Podaj a: "))

b = int(input("Podaj b: "))

c = int(input("Podaj c: "))

obw = a + b + c
pobw = obw/2
pole = (pobw * ((pobw - a) * (pobw - b) * (pobw - c)))** 0.5

print(f" Obwód trjkąta: {obw} \n pole trójkąta: {pole}")