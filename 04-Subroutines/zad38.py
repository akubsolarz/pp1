def f(palindrome):
    pal = ''
    for i in range(len(str(palindrome))-1,-1,-1):
        pal = pal + palindrome[i]
    if palindrome == pal:
        return True
    else:
        return False

print(f("radar")) 
print(f("12-11-21")) 
print(f("book")) 