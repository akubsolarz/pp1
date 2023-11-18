def f(number):
    sum = 0
    li = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,len(str(number))):
        for j in range(0,10):
            if j == int(str(number)[i]):
                li[j] += 1
                break
    for x in range(0,10):
        if li[x] >= 2:
            sum += x*li[x]
    print(sum)

f(1027)
f(230335)
f(513553007)