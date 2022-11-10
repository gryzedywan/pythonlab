l1 = [3,5,2,1,6]
l2 = [2,1,2,3,6]

l1.sort()
l2.sort()

l3 = []

for i in l1:
    for j in l2:
        if i <= j:
            l3.append(i)
        else:
            l3.append(j)

print(l3)