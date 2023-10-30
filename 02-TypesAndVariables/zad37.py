tekst = "Mr. John May, born on 1998-02-16" 
name = tekst[4:8]
Surname = tekst[9:12]
Initials = tekst[4] + tekst[9]
Born = tekst[22:]
print(f" name: {name} \n Surname: {Surname} \n inicial: {Initials} \n born: {Born}")