# Вам дан файл books.txt, который включает в себя названия книг,
# каждое на отдельной строке.

# Создайте программу, которая выводит, сколько слов содержит каждое название

with open("books.txt") as f:
    # your code goes here
    i = 1
    for line in f.readlines():
        print("Line", str(i) + ':', end=' ')
        print(str(len(line.split())) + " words")
        i += 1