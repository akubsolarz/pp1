def f(x,y):
    li = 0 
    for i in range(x,y+1):
        if i < 0:
            if i % 2 == 0:
                li += 1
    return li

print(f(-7,8))
print(f(-1,11))