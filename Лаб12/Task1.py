import json

def show_json(di):
    with open(di, "r") as jfile:
        text = json.load(jfile)
        for i in text:
            print(i, text[i])
    jfile.close()


def add_elem(di):
    with open(di, "r+") as jfile:
        text = json.load(jfile)
        rewrite = "Так"
        key = input("Введіть модель авто: ")
        if key in text:
            rewrite = input("Елемент з таким ключем вже існує! Перезаписати його?\n\
            (Введіть 'Так', щоб підтвердити,або щось інше, щоб відмовити): ")
        if rewrite == "Так":
            while True:
                text[key] = {}
                text[key]["Рік"] = input("Введіть рік випуску: ")
                if text[key]["Рік"].isdigit():
                    text[key]["Рік"] = int(text[key]["Рік"])
                    break
                print("Значення повинно бути числом!")
            while True:
                text[key]["Вартість"] = input("Введіть вартість: ")
                if text[key]["Вартість"].isdigit():
                    text[key]["Вартість"] = int(text[key]["Вартість"])
                    break
                print("Значення повинно бути числом!")
        jfile.close()
    with open(di, "w") as jfile:
        json.dump(text, jfile)
        print("Пара '{}' : '{}' додана".format(key, text[key]))
        jfile.close()



def del_elem(di):
    with open(di, "r") as jfile:
        text = json.load(jfile)
        jfile.close()
    key = input("Введіть модель авто: ")
    if key in text:
        val = text[key]
        del text[key]
        with open(di, "w") as jfile:
            json.dump(text, jfile)
            jfile.close()
        print("Пара '{}' : '{}' видалена".format(key, val))
    else:
        print("Такого ключа не існує!")


def search_json(di):
    with open(di, "r") as jfile:
        text = json.load(jfile)
        jfile.close()
    if text:
        set = int(input("Введіть номер поля, за яким ви хочете почати пошук: \n1. Модель.\n2. Рік випуску.\n3. Вартість.\n--> "))
        search = input("Введіть дані для пошуку: ")
        print("Ось що нам вдалось знайти:")
        for i in text.keys():
            if set==1 and search == i:
                print("Модель: '{}', Рік випуску: {}, Вартість: ${}".format(i, text[i]["Рік"], text[i]["Вартість"]))
            elif set == 2 and int(search) == text[i]["Рік"]:
                print("Модель: '{}', Рік випуску: {}, Вартість: ${}".format(i, text[i]["Рік"], text[i]["Вартість"]))
            elif set == 3 and int(search) == text[i]["Вартість"]:
                print("Модель: '{}', Рік випуску: {}, Вартість: ${}".format(i, text[i]["Рік"], text[i]["Вартість"]))
            elif set<1 or set>3:
                print("Невідоме поле!")
                break
    else:
        print("Словник пустий")

def aver_cost(di, year):
    with open(di, "r") as jfile:
        text = json.load(jfile)
        jfile.close()
    cost = 0
    n = 0
    for i in text:
        if year - text[i]["Рік"] > 6:
            cost += text[i]["Вартість"]
            n += 1
    print("Середня вартість автомобілів, «вік» яких перевищує 6 років: $" + str(cost / n))


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
namefile = "source.json"
with open(namefile, "w") as fsource:
    json.dump(cars, fsource)


print("Доступні такі команди: \n\
    [0] - завершити програму;\n\
    [1] - додати елемент до файлу;\n\
    [2] - видалити елемент з файлу;\n\
    [3] - вивести всі елементи файлу;\n\
    [4] - знайти елементи файлу за даними;\n\
    [5] -  визначити середню вартість автомобілів, «вік» яких перевищує 6 років;")
while True:
    choose = int(input("Введіть індекс операції: "))
    if choose == 0:
        print("Завершення...")
        break
    elif choose == 1:
        add_elem(namefile)
    elif choose == 2:
        del_elem(namefile)
    elif choose == 3:
        show_json(namefile)
    elif choose == 4:
        search_json(namefile)
    elif choose == 5:
        aver_cost(namefile, 2024)
    else:
        print("Невідома операція!")