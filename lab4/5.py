punkty = [22,50,23,12,5,12,47,48,32,12,1,22,34,45,33]

x = float(input('podaj pkt '))
if x in punkty:
    print('indeks to: ',punkty.index(x))
else:
    print('nima')

print(sum(punkty))
srednia = sum(punkty)/15
print(srednia)

ponad = 0
ponizej = 0
for i in punkty:
    if i > srednia:
        ponad = ponad + 1
    else:
        ponizej = ponizej + 1

print('ponizej: ',ponizej)
print('ponad: ',ponad)

