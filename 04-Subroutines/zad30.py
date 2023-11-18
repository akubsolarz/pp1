def f(number, even):
    sum = 0
    if even == True:
        for i in range(0,len(str(number))):
            if int(str(number)[i]) % 2 == 0:
                sum += int(str(number)[i])
    else:
        for i in range(0,len(str(number))):
            if int(str(number)[i]) % 2 != 0:
                sum += int(str(number)[i])
    print(sum)

f(3124,True)
f(3124,False)
f(20576,False)
f(20576,True)
f(13115,True)