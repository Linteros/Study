# Дан список зарплат, возьмите премию и увеличьте все зарплаты на эту сумму

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())


def bon(x):
    return x + bonus


print(list(map(bon, salaries)))

# результат должен быть явно преобразован в список, если вы хотите его распечатать