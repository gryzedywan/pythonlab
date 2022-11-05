x = [1,2,3,4,5,6,7,8,9,10]
x_ost = x[-3:]
print(x_ost)
licznik = 0
for i in x_ost:
    x.insert(licznik,i)
    licznik += 1
print(x)
del x[-3:]
print(x)

y = x
y[1] = 6644

print(x)
print(y)