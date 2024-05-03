# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.


# аутизм. это эквивалентно arr == arr[ : : -1]
def pal(arr):
    arr = str(arr)
    s = 0
    for i in range(len(arr) // 2):
        if arr[i] == arr[-(i+1)]:
            s += 1
            if s == len(arr) // 2:
                return True
        else:
            return False


# вариант здорового человека
def pal1(arr):
    arr = str(arr)
    if arr == arr[::-1]:
        return True
    else:
        return False


def my_max(arr):
    x = 0
    for i in arr:
        if i > x:
            x = i
    return x


b = []
for i in range(100, 1000):
    for n in range(100, 1000):
        if pal1(i * n):  # красивый код
            b.append(i * n)

print(my_max(b))