litera = input("podaj litere")

if litera in "abcdefghijklmnopqrstuvwxyz":
    print(litera.upper())
elif litera in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(litera.lower())
else:
    print("to nie jest litera")
