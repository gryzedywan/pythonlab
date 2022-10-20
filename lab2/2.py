litera = input("podaj litere: ")

if len(litera) == 1:
    if litera in "abcdefghijklmnopqrstuvwxyz":
        print("litera jest mala")
    elif litera in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("litera jest duza")
    else:
        print("to nie jest litera")
else:
    print("za dlugie")
