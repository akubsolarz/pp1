def f(password):
    liczba_ruznic = 0
    stri = str(password)
    stwierdzone_inne = 0
    if len(str(password)) >= 6:
        for i in range(0,len(str(password))):
            for j in range(0,i+1):
                if stri[i] != stri[j]:
                    liczba_ruznic += 1
                if liczba_ruznic == i:
                    stwierdzone_inne += 1
                    liczba_ruznic = 0
    if stwierdzone_inne == len(str(password)) and stwierdzone_inne != 0:
        print(True)
    else:
        print(False)

f("ax15")
f("book123")
f("A2water3")
f("qwerty")
f("")
