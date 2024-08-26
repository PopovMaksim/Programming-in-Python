def sumxy():
    x = int(input("Введіть x: "))
    y = int(input("Введіть y>=x: "))
    while y<x:
        y = int(input("y повинен бути не менше x! Введіть y: "))
    z=0
    for i in range(x, y+1):
        if i%2==0:
            z+=i
    return z