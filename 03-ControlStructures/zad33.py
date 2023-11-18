num1 = input("Enter decimal number: ")

while int(num1) >= 1: 
    num2 = int(num1) % 2
    num1 = (int(num1) // 2)
    print(str(num2[::-1]))