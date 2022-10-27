n = int(input('liczba studentow: '))
y = 0
z = n

while n != 0:
    x = float(input("liczba pkt studenta: "))
    y = y + x
    n = n - 1

print(y/z)