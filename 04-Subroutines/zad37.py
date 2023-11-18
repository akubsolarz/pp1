def f(n):
    l1 = 0
    l2 = 1
    if n == 1:
        print(l1)
    if n == 2:
        print(l2)
    if n > 2:
        for i in range(1,n-1):
            l3 = l1 + l2
            l1 = l2
            l2 = l3
        print(l3)

f(5) 
f(9)
