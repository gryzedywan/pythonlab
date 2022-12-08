def znaki(string):
    dic1 = {x: string.count(x) for x in string}
    return dic1
print(znaki('znaki napisu'))
