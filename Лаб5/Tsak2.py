n = 7
mass = []
for i in range(n):
    for j in range(n):
        mass.append(-n + 1 + i + j)
        print(str(mass[-1]).rjust(2), end=" ")
    print()