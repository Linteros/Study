# Генераторы - это тип итерируемых объектов, как списки или кортежи.
# В отличие от списков, они не позволяют индексирование с произвольными индексами,
# но их можно все равно перебирать с помощью for. Их можно создать с помощью функций и оператора yield


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)

# Оператор yield используется для определения генератора, заменяя возврат функции,
# чтобы предоставить результат его вызывающему без уничтожения локальных переменных
