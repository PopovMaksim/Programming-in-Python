from itertools import groupby

import pandas as pd


cars = {
    "Модель" : ["Tesla Model 3", "Toyota Camry", "Honda Civic", "Ford Mustang", "BMW 3 Series", "Mercedes-Benz C-Class", "Audi A4", "Nissan Altima", "Hyundai Sonata", "Kia K5"],
    "Вартість":[35000, 32000, 21000, 20000, 40000, 45000, 38000, 24000, 23000, 22000]
}

df = pd.DataFrame(cars)

print(df)

print("Загальна вартість усіх автомобілів: $",df["Вартість"].sum())
print("Середня вартість автомобіля: $",df["Вартість"].mean())
df["Ціновий діапазон"] = pd.cut(df["Вартість"], bins = [0, 25000, 35000, 50000], labels=["Бюджетні", "Середній клас", "Люкс"])
group = df.groupby("Ціновий діапазон").size()

print(group)
