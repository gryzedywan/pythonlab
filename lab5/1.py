values = [10,20,30]
keys = ['ten','twenty','thirty']

D = (dict(zip(keys,values)))
print(D)

E = (dict(ten = 10, twenty = 20, thirty = 30))
print(E)

D.update(E)
print(D)