def f(text) :
    stri = ''
    if len(text) > 1:
        stri = stri + text[0]
        for i in range(1,len(text)):
            stri += '-' + text[i]
    else:
        stri = text
    print(stri)
f("Univesity")
f("UE")
f("x")
f("")