def openfile(file_name, mode):

    try:

        file = open(file_name, mode)

    except:

        print("Не вдалося відкрити файл '" + file_name + "'!")

        return None

    else:

        print("Файл '" + file_name + "' Відкрився!")

        return file

file1_name = "TF15_1"
file2_name = "TF15_2"

file1 = openfile(file1_name, "w")
if file1:
    text = "Тут знаходиться рядок.\nЗнайдіть симетричні слова: мама, казка, потоп, кіт, око, целюлоза"
    file1.write(text)
    file1.close()

file1 = openfile(file1_name, "r")
file2 = openfile(file2_name, "w")
if file1 and file2:
    buf = ""
    for i in file1.read():
        if not (i.isdigit() or i.isalpha()):
            buf = buf + " "
        else:
            buf = buf + i
    print(buf)
    words = buf.split()
    for word in words:
        for i in range(len(word)):
            if i>=len(word)/2:
                file2.write(word+", ")
                break
            elif word[i].lower() != word[-i-1].lower():
                break
    file2.close()
    file1.close()

file2 = openfile(file2_name, "r")
if file2:
    for word in file2.read().split():
        print(word)
    file2.close()
