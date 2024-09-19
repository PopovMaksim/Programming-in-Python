def task1(list1):
    print("--Завданя 1--\nСписок має вигяд: ", list1)
    while True:
        pos = int(input("Введіть непарну позицію, куди необхідно вставити елемент: "))
        if pos%2==0:
            print("Позиція парна, спробуйте ще раз!")
        elif pos>len(list1):
            print("Позиція перевищує розмір списку! Спробуйте ще раз!")
        else:
            break

    list1.insert(pos, input("Введіть що необхідно вставити в список: "))
    print("Список має вигяд: ", list1)

def task2():
    n = int(input("--Завдання 2--\nВведіть кількість елементів у списку:"))
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
    print("--Завдання 3--")
    word = input("Введіть слово з латинських літер: ")
    set1 = set(word)
    print("Перші входження: ", set1)

task1([0, 1, 2, 3, 4])
task2()
task3()