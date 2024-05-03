# Примите число N в качестве ввода и запишите числа
# от 1 до N в файл "numbers.txt", каждое число на отдельной строке.

n = int(input())

file = open("numbers.txt", "w")

# your code goes here
for i in range(1, n+1):
    file.write(str(i) + "\n")
file.close()

f = open("numbers.txt", "r")
print(f.read())
f.close()