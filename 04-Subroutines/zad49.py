def f(dice):
    num = [0,0,0,0,0,0]
    wy = 0
    for i in range(0,len(dice)):
        for j in range(1,7):
            if int(dice[i]) == j:
                num[j-1] += 1
                break
    for i in range(1,6):
        if num[i-1] < num[i]:
            wy = i+1
    print(wy)
f("5233165554211")
f("2133")