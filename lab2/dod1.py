a = input("podaj liczbe")

lista = []
for i in a:
    lista.append(int(i))

lista.reverse()
b = max(lista) + 1

if b == 2:
    wynik = 0
    c = 0
    for i in lista:
        print(lista)
        print(i)
        wynik = i * b ** c + wynik
        print(wynik)
        c = c + 1

print(wynik)
