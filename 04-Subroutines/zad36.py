def f(detector):
    li = 0
    for i in range(0,len(detector)):
        if detector[i] == '+':
            li += 1
        else:
            li -= 1
        if li >= 3:
            print(True)
            break
    if li < 3:
        print(False)

f("+-+++-+---") 
f("+-+-+-+-")  
f("+-++-+--") 
f("+-++-++-+---") 