def f(card_number):
    print('"', end = '')
    for i in range(0,16):
        if i < 2 or i > 11:
            print(card_number[i], end = '')
        else:
            print('*', end='')
    print('"', end = '')