print(
'''1. dodawanie
2. odejmowanie
3. mnozenie
4. dzielenie
5. potegowanie''')

a = int(input('numer operacji: '))
b = float(input('podaj argument1: '))
c = float(input('podaj argument2: '))

if a == 1:
    wynik = b + c
elif a == 2:
    wynik = b - c
elif a == 3:
    wynik = b * c
elif a == 4:
    wynik = b / c
elif a == 5:
    wynik = b ** c
else:
    wynik = "bledny nr operacji"

print(wynik)