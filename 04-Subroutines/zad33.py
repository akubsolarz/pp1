def  f(n):
    if n >= 1:
        print('*', end='')
    for i in range(0,n-1):
        print('/', end='*')
    print('')
f(4) 
f(1) 