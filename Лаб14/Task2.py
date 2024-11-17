import numpy as np
import csv

import matplotlib.pyplot as plt


x = []
y = []
z = []
try:
    with open("source_file.csv") as file1:
        reader = csv.DictReader(file1, delimiter=",")
        source = list(reader)
        for key in source[0].keys():
            if key[:4].isdigit():
                x.append(key[:4])
                y.append(round(float(source[0][key]),2))
                z.append(round(float(source[1][key]),2))

except FileNotFoundError:
    print("Файл 'source_file.csv' не знайдено!")

np.array(x)

np.array(y)

np.array(z)

plt.plot(x, z, label='Poland', color = "red")
plt.plot(x, y, label='Ukraine', color = "yellow")
plt.title('Life expectancy at birth, total', fontsize=15, color='blue')   # назва графіка
plt.xlabel('Year', fontsize=12, color='red') # позначення вісі абсцис
plt.ylabel('Indicator', fontsize=12, color='red') # позначення вісі ординат
plt.legend()
plt.grid(True)
plt.show()

mod = int(input("Введіть 0, якщо хочете побудувати діаграму для України, або інший символ щоб для Польші: "))
if mod==0:
    s = y
    country = "Ukraine"
else:
    s = z
    country = "Poland"

xr = range(len(s))

ax = plt.gca()
ax.bar(xr, s)
ax.set_xticks(xr)
ax.set_xticklabels(x)
ax.set_title("Life expectancy at birth, total in "+country)
plt.show()