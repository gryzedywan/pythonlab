#5 na wejsciu tylko parzyste w liscie

n = 5
lista = []

for i in range(n):
    x = int(input('podaj liczbe: '))
    if x % 2 == 0:
        lista.append(x)

print(lista)