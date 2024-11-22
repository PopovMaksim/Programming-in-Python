import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

wordnet_lemmatizer = WordNetLemmatizer()
try:
    with open("source.txt", "r") as f:
        text = f.read().lower()
        # токенізація
        words = nltk.word_tokenize(text)

        # лематизація
        lemmatized = [wordnet_lemmatizer.lemmatize(w) for w in words]

        # стемінг
        ps = PorterStemmer()
        stemed = [ps.stem(w) for w in lemmatized]

        # вилучення стоп слів і пунктуації
        stop_words = set(stopwords.words("english"))
        without_stop_words_punctuation = [word for word in stemed if not word in stop_words and (word.isalpha() or word.isalnum())]

        delimiter = " "
        new_text = delimiter.join(without_stop_words_punctuation)
        with open("new_text.txt", "w") as f2:
            f2.write(new_text)
            print("Відредагований текст успішно записано в файл!")


except FileNotFoundError:
    pprint("Файл не знайдено!")