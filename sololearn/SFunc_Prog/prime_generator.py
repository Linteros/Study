# Создайте функцию-генератор, которая будет принимать два числа в качестве аргументов
# и выводить простые числа в заданном диапазоне


def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def primeGenerator(a, b):
    for i in range(a, b):
        if isPrime(i):
            yield i


f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))