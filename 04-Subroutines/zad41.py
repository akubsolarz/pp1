def f(n):
    li=0
    i=0
    while li < n:
        czy=0
        for j in range (1,i+1):
            if i%j == 0:
                czy += 1
        if czy == 2:
            print(i, end=' ')
            li += 1
        i += 1
f(20)