wiek = int(input('wprowadz wiek: '))

if wiek < 4:
    cena = 0
    print("bilet jest bezplatny")
elif wiek >= 4 and wiek <= 18:
    cena = 10
    print("cena biletu: ", cena)
else:
    cena = 20
    print("cena biletu: ",cena)
