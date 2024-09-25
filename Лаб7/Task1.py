def show_dict(di):
    if di:
        print("Всі моделі автомобілів у словнику:")
        for i in di:
            print("Модель: '{}', Рік випуску: {}, Вартість: ${}".format(i, di[i]["Рік"], di[i]["Вартість"]) )
    else:
        print("Словник пустий!")


def add_elem(di):
    rewrite = "Так"
    key = input("Введіть модель авто: ")
    if key in di:
        rewrite = input("Елемент з таким ключем вже існує! Перезаписати його?\n\
        (Введіть 'Так', щоб підтвердити,або щось інше, щоб відмовити): ")
    if rewrite == "Так":
        while True:
            di[key] = {}
            di[key]["Рік"] = input("Введіть рік випуску: ")
            if di[key]["Рік"].isdigit():
                di[key]["Рік"] = int(di[key]["Рік"])
                break
            print("Значення повинно бути числом!")
        while True:
            di[key]["Вартість"] = input("Введіть вартість: ")
            if di[key]["Вартість"].isdigit():
                di[key]["Вартість"] = int(di[key]["Вартість"])
                break
            print("Значення повинно бути числом!")
        print("Пара '{}' : '{}' додана".format(key, di[key]))


def del_elem(di):
    key = input("Введіть модель авто: ")
    if key in di:
        val = di[key]
        del di[key]
        print("Пара '{}' : '{}' видалена".format(key, val))
    else:
        print("Такого ключа не існує!")


def sort_dict(di):
    if di:
        sort_di = {key: dict[key] for key in sorted(di)}
        print("Відсортований словник за назвами моделей: ")
        for i in sort_di:
            print("Модель: '{}', Рік випуску: {}, Вартість: ${}".format(i, di[i]["Рік"], di[i]["Вартість"]) )
    else:
        print("Словник пустий")

def aver_cost(di, year):
    cost = 0
    n = 0
    for i in di:
        if year - di[i]["Рік"] >6:
            cost+= di[i]["Вартість"]
            n+=1
    print("Середня вартість автомобілів, «вік» яких перевищує 6 років: $"+str(cost/n))


cars = {
    "Tesla Model 3": {"Рік": 2017, "Вартість": 35000},
    "Toyota Camry": {"Рік": 2023, "Вартість": 25000},
    "Honda Civic": {"Рік": 2022, "Вартість": 20000},
    "Ford Mustang": {"Рік": 1964, "Вартість": 20000},
    "BMW 3 Series": {"Рік": 2021, "Вартість": 40000},
    "Mercedes-Benz C-Class": {"Рік": 2016, "Вартість": 45000},
    "Audi A4": {"Рік": 2023, "Вартість": 38000},
    "Nissan Altima": {"Рік": 2022, "Вартість": 24000},
    "Hyundai Sonata": {"Рік": 2021, "Вартість": 23000},
    "Kia K5": {"Рік": 2015, "Вартість": 22000}
}
print("Доступні такі команди: \n\
    [0] - завершити програму;\n\
    [1] - додати елемент до словника;\n\
    [2] - видалити елемент зі словника;\n\
    [3] - вивести всі елементи словника;\n\
    [4] - вивести всі елементи словника у відсортованому порядку;\n\
    [5] -  визначити середню вартість автомобілів, «вік» яких перевищує 6 років;")
while True:
    choose = int(input("Введіть індекс операції: "))
    if choose == 0:
        print("Завершення...")
        break
    elif choose == 1:
        add_elem(cars)
    elif choose == 2:
        del_elem(cars)
    elif choose == 3:
        show_dict(cars)
    elif choose == 4:
        sort_dict(cars)
    elif choose == 5:
        aver_cost(cars, 2024)
    else:
        print("Невідома операція!")


