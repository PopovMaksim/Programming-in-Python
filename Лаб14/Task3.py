import numpy as np
import csv

import matplotlib.pyplot as plt


x = []
y = []
try:
    with open("source_file.csv") as file1:
        reader = csv.DictReader(file1, delimiter=",")
        source = list(reader)
        for key in source[0].keys():
            if key[:4].isdigit():
                x.append(key[:4])
                y.append(round(float(source[0][key]),2))

except FileNotFoundError:
    print("Файл 'source_file.csv' не знайдено!")

np.array(x)

np.array(y)


fig, ax = plt.subplots()

ax.pie(y, labels = x, autopct='%1.0f%%')
ax.axis("equal")
ax.set_title("Life expectancy at birth, total in Ukraine")
plt.show()