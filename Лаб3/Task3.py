string1 = input("Введіть речення: ")

words = string1.split()
words.sort(key=lambda item: len(item))
print("Слова в порядку неспадання їх довжини: ")
for word in words:
    print(word)