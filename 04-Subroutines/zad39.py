def f(sentence):
    for i in range(0,len(str(sentence))):
        if str(sentence[i]) != ' ':
            print(str(sentence[i]),end='') 
    print('')

f("integrated development environment") 
f("A programming language is a system of notation for writing computer programs") 
