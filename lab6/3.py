def max(*args):
    if len(args) == 0:
        return None
    m = args[0]
    for i in args[1:]:
        if i > m:
            m = i
    return m
wynik = max(31,4,19,23)
print(wynik)
print(max())
print(max('w','z'))