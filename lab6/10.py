import random

def gra():
    proby = 0
    x = random.randint(-5,5)
    while True:
        a = int(input('podaj liczbe: '))
        if a == x:
            proby += 1
            return f'udalo sie, liczba prob to {proby}'
        elif a > x:
            proby += 1
            print(f'za duzo, liczba prob to {proby}')
        elif a < x:
            proby += 1
            print(f'za malo, liczba prob to {proby}')

print(gra())

