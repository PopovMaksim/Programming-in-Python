import nltk
from nltk.corpus import stopwords
import re
import string
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter #словник, який дозволяє рахувати кількість незмінюваних об'єктів (напр. рядки)


try:
    File = open('edgeworth-parents.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

text = File.read()
def count_words(text):
    sentences = nltk.sent_tokenize(text)  # токенізація по реченням
    k_words = 0
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        # words - список зі словами
        k_words += len(words)
    return k_words

def most_used_words(text):
    text1 = text.split() #cписок зі словами
    cnt = Counter(text1) #підрахунок слів
    cort = cnt.most_common(10)
    x = [cort[el][0] for el in range(len(cort))] #слова
    y = [cort[el][1] for el in range(len(cort))] #к-ть повторень у тексті
    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова") #підписи по осям
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()

print("Кількість слів:",count_words(text))
most_used_words(text)

stop_words = set(stopwords.words("english"))
words = nltk.word_tokenize(text)
without_stop_words = [word for word in words if not word.lower() in stop_words and (word.isalpha() or word.isalnum())]
delimiter = " "
new_text = delimiter.join(without_stop_words)
print("Кількість слів без стоп-слів і пунктуації:",count_words(new_text))
most_used_words(new_text)

File.close()
