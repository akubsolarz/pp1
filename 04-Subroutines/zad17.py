def licz(n1,n2,n3):
    if n1 != n2 and n1 != n3 and n2 != n3:
        print(f"Numbers {n1}, {n2}, and {n3} are different")
        return True
    return False

num1 = int(input("liczba 1:" ))
num2 = int(input("liczba 2:" ))
num3 = int(input("liczba 3:" ))

print(licz(num1,num2,num3))


