imiona = ['Kasia', 'Tomek', 'Jan', 'Ola', 'Jerzy', 'Marek', 'Piotr', 'Zuzia', 'Bartek', 'Jacek']

imiona[2] = 'Wojtek'

imiona.insert(4,'Edward')

del imiona[6]
print(imiona)

ulub = ['Monika','Adrian','Dominika']
licznik = 0

for i in ulub:
    imiona.insert(licznik,i)
    licznik += 1

print(imiona)

while True:
    x = input('co usunac ')
    x_cap = x.capitalize()
    print(x_cap)
    if x_cap in imiona:
        imiona.remove(x_cap)
        break
    else:
        print('zle imie ')

imiona[-1] = 'Konrad'

print(imiona)
print(imiona[0:3])
print(imiona[-3:])

imie = input('podaj imie ')
print(imie in imiona)

imiona.sort()
print(imiona)

print(imiona[::-1])

dlugosc = int(len(imiona))
polowa = int(dlugosc/2)

for i in range(polowa,dlugosc):
    imiona.pop()
print('liczba elementow: ', len(imiona))