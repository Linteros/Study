# После того как файл был открыт и использован, вы должны его закрыть.
# Это делается с помощью метода close объекта файла.

file = open("filename.txt", "w")
# do stuff to the file
file.close()