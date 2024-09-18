def task1():
    n = int(input("--Завдання1--\nВведіть кількість елементів у списку:"))
    list1 = []
    print("Введіть елементи списку:")
    for i in range(n):
        list1.append(None)
        list1.append(input())
    print(list1)

def task2():
    n = int(input("--Завдання2--\nВведіть кількість елементів у списку:"))
    list2 = []
    print("Введіть елементи списку(тільки числа): ")
    for i in range(n):
        a = input()
        while not a.isdigit():
            print("Це не число! введіть число")
        list2.append(a)
    list2[list2.index(max(list2))], list2[list2.index(min(list2))] = list2[list2.index(min(list2))], list2[list2.index(max(list2))]
    print(list2)

def task3():
    print("--Завдання3--")
    word = input("Введіть слово з латинських літер: ")
    set1 = set(word)
    print("Перші входження: ", set1)

task1()
task2()
task3()