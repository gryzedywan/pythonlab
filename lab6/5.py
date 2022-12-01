def dodawanie(a,b):
    return a + b

def odejmowanie(a,b):
    return a - b

def mnozenie(a,b):
    return a * b

def dzielenie(a,b):
    return a / b

kalkulator = {'+' : dodawanie,
              '-' : odejmowanie,
              '*' : mnozenie,
              '/' : dzielenie}

print(kalkulator['+'](4,3))