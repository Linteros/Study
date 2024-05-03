# Строки также являются объектами и имеют методы, при помощи
# которых можно делать практически всё

# Все строки, используемые вами в программах, являются объектами класса str.
# Некоторые полезные методы этого класса продемонстрированы на примере ниже.
# Чтобы посмотреть весь список методов, выполните help(str).

name = 'Swaroop' # Это объект строки

if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')

if 'a' in name:
    print('Да, она содержит строку "a"')

if name.find('war') != -1:
    print('Да, она содержит строку "war"')

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))

# Здесь мы видим сразу несколько методов строк в действии. Метод startswith служит для
# того, чтобы определять, начинается ли строка с некоторой заданной подстроки. Оператор
# in используется для проверки, является ли некоторая строка частью данной строки.
# Метод find используется для определения позиции данной подстроки в строке; find возвращает -1,
# если подстрока не обнаружена. В классе str также имеется отличный метод для объединения (join)
# элементов последовательности с указанной строкой в качестве
# разделителя между элементами, возвращающий большую строку, сгенерированную таким образом.