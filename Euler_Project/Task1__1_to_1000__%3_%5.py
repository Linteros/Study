# Задача 1
# Числа, кратные 3 или 5
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5


x = []
y = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 ==0:
        x.append(i)  # Это для того, чтобы вывести все эти числа
        y += i

print('Числа от 1 до 1000 кратные 3 или 5:', x)
print('Сумма этих чисел', y)