# Вам нужно создать программу для чтения заданного числа символов из файла.
# Примите число N в качестве ввода и выведите первые N символов из файла books.txt.

# Данный код открывает файл books.txt. Используйте объект file для чтения содержимого файла.

file = open("books.txt")
# your code goes here

N = int(input())
print(file.read(N))

file.close()