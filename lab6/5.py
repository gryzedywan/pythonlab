def dodawanie(a,b):
    return a + b

def odejmowanie(a,b):
    return a - b

def mnozenie(a,b):
    return a * b

def dzielenie(a,b):
    return a / b

kalkulator = {'dodawanie' : dodawanie(),
              'odejmowanie' : odejmowanie(),
              'mnozenie' : mnozenie(),
              'dzielenie' : dzielenie()}

print(kalkulator)