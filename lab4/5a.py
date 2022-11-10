import random

ile = 15

punkty=[round(random.uniform(0,50),2) for a in range(ile)]
print(punkty)

x = float(input('podaj punkty '))

if x in punkty:
    print('indeks to', punkty.index(x))
else:
    print('brak')

srednia = sum(punkty)/ile
print('srednia to ', srednia)

ponad = []
for i in punkty:
    if i > srednia:
        ponad.append(i)

ponizej = [i for i in punkty if i < srednia]

print(f'liczby ponad to {ponad} oraz jest ich {len(ponad)}')
print(f'liczby ponizej to {ponizej} oraz jest ich {len(ponizej)}')

