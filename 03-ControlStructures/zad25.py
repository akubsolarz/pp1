num1 = int(input("Number of products purchased: "))
num2 = int(input("Product price: "))

if num1 > 2:
    print(f"Amount to pay: {num2*2+((num1-2)*num2)*0.75}")
else: 
    print(f"Amount to pay: {num2*num1}")