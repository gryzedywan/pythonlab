def literki(string):
    male = 0
    duze = 0
    pozostale = 0
    slownik = {}
    for i in string:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            male += 1
        elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            duze += 1
        else:
            pozostale += 1

    slownik = {'male' : male,'duze' : duze,'pozostale' : pozostale}
    return slownik

print(literki('andrzej1'))
print(literki('577hshb;;;'))
print(literki('AHSsjdS;;;..'))