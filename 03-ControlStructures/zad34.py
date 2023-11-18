nump = int(input("Enter the amount in PLN: "))
num1 = nump
if num1 >= 5:
    ti5 = num1 // 5
    num1 = num1 - ti5*5
else:
    ti5 = 0
if num1 >= 2:
    ti2 = num1 // 2
    num1 = num1 - ti2*2
else:
    ti2 = 0
if num1 >= 1:
    ti1 = num1 // 1
else:
    ti1 = 0
    
print(f"The amount of PLN {nump} in coins: \n5 zł – {ti5}  \n2 zł – {ti2}  \n1 zł – {ti1} ")