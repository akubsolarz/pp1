a = 4
b = 15

for i in range(1,a+1):
    if i == 1 or i == a:
        for j in range(1,b+1):
            print('*', end='')
    else:
        for k in range(1,b+1):
            if k == 1 or k == b:
                print('*', end='')
            else:
                print(' ', end='')
    print('')

