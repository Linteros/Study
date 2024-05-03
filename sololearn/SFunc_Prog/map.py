def add_five(x):
    return x + 5


# map применяет функцию к каждому элементу списка и возвращает полученное значение

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x + 5, nums))
print(result)

# результат должен быть явно преобразован в список, если вы хотите его распечатать