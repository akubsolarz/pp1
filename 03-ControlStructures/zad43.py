l1 = 0
l2 = 1
for i in range(1,21):
    l3 = l1 + l2
    if l3 == 1:
        print(f"{l1} {l2}", end=' ')
    l1 = l2
    l2 = l3
    print(l3, end=' ')