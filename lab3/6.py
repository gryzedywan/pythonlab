n = int(input('liczba studentow: '))
y = 1
suma = 0

while y < n + 1:
    x = float(input(f"liczba pkt studenta {y}: "))
    if x < 0 or x > 100:
        continue
    suma = suma + x
    y = y + 1

print(suma/n)