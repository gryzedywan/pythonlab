def znaki(string):
    dic1 = {}
    for i in string:
        dic1[i] = dic1.get(i,0) + 1
    #    if i in dic1:
     #       dic1[i] = dic1[i] + 1
      #  else:
       #     dic1[i] = 1


    return dic1


slownik = znaki('znaki napisu')
lista_kluczy = sorted(slownik)

for i in lista_kluczy:
    print(i, slownik.get(i))

print(znaki('znaki napisu'))