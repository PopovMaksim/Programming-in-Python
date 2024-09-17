n = int(input("Введіть кількість елементів у масиві: "))
print("Введіть елементи масиву: ")

mass = [int(input()) for i in range(n)]

print("Від'ємні елементи починаючи з кінця: ")
for elem in mass[::-1]:
    if elem<0:
        print(elem, end=" ")