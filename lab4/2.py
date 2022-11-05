import random

zestaw_1 = []
n = int(input('podaj liczbe elementow'))

for i in range(n):
    zestaw_1.append(random.randint(1,10))

zestaw_2 = []
m = int(input('podaj liczbe elementow'))

for i in range(m):
    zestaw_2.append(random.randint(5,15))

print(zestaw_1)
print(zestaw_2)

x = int(input('podaj liczbe '))
if x in zestaw_1:
    print('liczba z zestawu 1')
elif x in zestaw_2:
    print('liczba z zestawu 2')
else:
    print('nie ma w obu')

zestaw_1_2 = zestaw_1 + zestaw_2

zestaw_1_2.sort()
print(zestaw_1_2)
