def find(a,l):
    l1 = []
    ind = 0
    for i in l:
        if i == a:
            l1.append(ind)
        ind += 1
    return l1

l2 = [4,2,1,46,4,2,4]
print(find(4,l2))