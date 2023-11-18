def f(binary_number):
    li = 0
    for i in range(0,len(binary_number)):
        if binary_number[i] != '1' and binary_number[i] != '0':
            li += 1
    if li == 0:
        return True
    else:
        return False
           
        
print(f("101101"))
print(f("1311a10100"))