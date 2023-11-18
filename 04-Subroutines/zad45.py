def f(expression):
    stri = str(expression)
    sum = int(stri[0])
    for i in range(0,len(stri)):
        if stri[i] == '-':
            sum = sum - int(stri[i+1])
        elif stri[i] == '+':
            sum = sum + int(stri[i+1])
    print(sum)

f("2+3")
f("3+8+1")
f("2+3-4+5-0")