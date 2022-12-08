def dodawanie(a,b):
    return a + b

def odejmowanie(a,b):
    return a - b

def mnozenie(a,b):
    return a * b

def dzielenie(a,b):
    if b != 0:
        return a/b
    else:
        return 'nie dziel przez 0'

dzialania = {'+': dodawanie,
             '-': odejmowanie,
             '*': mnozenie,
             '/': dzielenie}

print(dzialania['+'](5,5))

