import math

def kwadratowe(a, b = 0, c = 0):
    delta = b**2 - 4*a*c
    if a != 0:
        if delta > 0:
            pdelta = math.sqrt(delta)
            x1 = (-b + pdelta) /2 * a
            x2 = (-b - pdelta) / 2 * a
            return x1,x2
        elif delta == 0:
            x1 = (-b)/2 * a
            return x1
        else:
            return ('Brak rozwiązań')
    else:
        return 'a mniejsze od 0, blad'
print(kwadratowe(1,2,-3))
print(kwadratowe(4,2,-4))
print(kwadratowe(0,0,242))