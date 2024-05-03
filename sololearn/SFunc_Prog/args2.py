# Напишите функцию, которая определяет минимальное значение из любого числа переменных


def my_min(x, *args):
    for i in args:
        if i < x:
            x = i
    return x


print(my_min(8, 13, 4, 42, 120, 7))