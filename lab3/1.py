a = int(input('podaj a'))
b = int(input('podaj b'))

if a > b:
    while b <= a:
        print(b)
        b = b + 1
else:
    while a <= b:
        print(a)
        a = a + 1
