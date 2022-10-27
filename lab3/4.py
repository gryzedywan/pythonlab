x = int(input("liczba x: "))
y = int(input("liczba y: "))

if x > y:
      x,y = y,x

while x <= y:
    if x % 2 == 1:
        x += 1
        continue
    print(x)
    x += 1
    '''if x % 2 == 0:
        print(x)
        x += 1
    else:
        x += 1'''