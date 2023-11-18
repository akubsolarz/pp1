def litera(n,text):
    li=0
    for i in range(0,len(text)):
        if text[i] == n:
            li += 1
    print(text)
    print(f"The number of letter '{n}': {li}")