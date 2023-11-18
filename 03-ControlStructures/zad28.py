ean = input("Enter EAN-13 article number: ")

if len(ean) == 13:
    if ean[0:3] ==  "590":
        print("Article number is correct\nArticle manufactured in Poland")
    else:
        print("incorect")
else: 
    print("EAN-13 is incorect")