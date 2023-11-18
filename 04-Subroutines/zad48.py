def  f(product_code):
    stri = str(product_code)
    sum = int(stri[0]) + int(stri[1]) + int(stri[2])
    if sum % 7 == int(stri[3]):
        print(True)
    else:
        print(False)
f("1082")
f("2035") 
f("1114") 
f("7071") 