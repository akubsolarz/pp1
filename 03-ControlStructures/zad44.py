li=0
num = 1 
sum = 0
while num != 0:
    num = int(input("Enter number: "))
    li += 1
    sum = sum + num
if num == 0:
    print(f"RESULT: Quantity={li-1}, Sum={sum}, Mean={sum//(li-1)}")
