def sum(n):

    if n <= 0:
        return 0
    
    if n > 0:
        return n + sum(n-1)
    
print(sum(10))

suma=0
for i in range(1,11):
    suma += i
print(suma)