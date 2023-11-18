def f(amount_to_pay):
    num1 = amount_to_pay
    if num1 >= 5:
        ti5 = num1 // 5
        num1 = num1 - ti5*5
    else:
        ti5 = 0
    if num1 >= 2:
        ti2 = num1 // 2
        num1 = num1 - ti2*2
    else:
        ti2 = 0
    if num1 >= 1:
        ti1 = num1 // 1
    else:
        ti1 = 0
    sum = ti5 + ti2 + ti1
    print(sum)

f(23)
f(8)
f(2)
f(0)