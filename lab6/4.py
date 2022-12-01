def f1(**kwargs):
    if 'end' in kwargs:
        endf1 = kwargs['end']
    else:
        endf1 = '\n'
    for key, value in kwargs.items():
        print(key, value, endf1)

f1(par1 = 1, par2 = 2,end = 45221)