# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

# Найдите сумму всех простых чисел меньше двух миллионов

i = 3
arrPrim = [2, 3]


def isPrime(x):
    for j in arrPrim[:]:
        if j < x**0.5:
            if x % j > 0:
                pass
            else:
                return False
        else:
            return True


# Функция, реализующая решето Эратосфена
def iprimes_upto(limit):
    is_prime = [True] * limit
    for n in range(2, limit):
        if is_prime[n]:
           yield n
           for i in range(n*n, limit, n): # start at ``n`` squared
               is_prime[i] = False

# Получаем все простые числа до 2 миллионов
primes = list(iprimes_upto(2000000))
print(sum(primes)) # выводим сумму> 142913828922

while i < 2000000:
    i += 2
    if iprimes_upto(i):
        arrPrim.append(i)

print(sum(arrPrim))  # 143042032112