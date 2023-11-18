def f(name):
    print(name[0],end='')
    for i in range(0,len(name)):
        if name[i] == ' ':
            print(name[i+1],end='')
    print('')

f("Internet of Things")
f("For Your Information")
f("Python")