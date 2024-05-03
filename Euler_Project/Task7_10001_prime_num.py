# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.

# Какое число является 10001-м простым числом?

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# аутизм
def isPrime2(x, g):
    if g == []:
        return False
    for i in g[-1:0:-1]:
        if x % g[i] > 0 and isPrime2(g[i-1], g[-2:0:-1]):
            return True
        else:
            return False


# решето Эратосфена
def isPrime3(x):
    for i in m[::-1]:
        if x % i > 0:
            pass
        else:
            return False
    return True


m = [2, 3]
n = 3

while len(m) < 10001:
    n += 2
    if isPrime3(n):
        m.append(n)

print(m[10000])