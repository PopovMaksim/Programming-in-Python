import csv

def minkey(key):
    if key[0:4].isdigit():
        return float(row[key])
    else:
        return float('inf')

def maxkey(key):
    if key[0:4].isdigit():
        return float(row[key])
    else:
        return float('-inf')
try:
    with open("source_file.csv") as file1:
        reader = csv.DictReader(file1, delimiter=",")
        for row in reader:
            minval = min(row, key=lambda k: minkey(k))
            maxval = max(row, key=lambda k: maxkey(k))
            print("Вміст csv файлу:\n", row)
            print("Мінімальне значення було в {} році: {}".format(minval[1:4], row[minval]))
            print("Максимальне значення було в {} році: {}".format(maxval[0:4], row[maxval]))
            with open("dest_file.csv", mode="w") as file2:
                writer = csv.DictWriter(file2, fieldnames=["Minimal", "Maximal"])
                writer.writeheader()
                writer.writerow({"Minimal": minval, "Maximal": maxval})
                writer.writerow({"Minimal":row[minval], "Maximal":row[maxval]})
                print("Дані занесені до файлу 'dest_file.cs'")
except:
    print("Файл 'source_file.csv' не знайдено!")
print("Завершення...")