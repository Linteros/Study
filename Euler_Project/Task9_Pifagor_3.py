# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

# a2 + b2 = c2
# Например, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

# from math import prod

coll = []

# for i in range(1, 500):
#     for j in range(1, i):
#         for k in range(1, j):
#             if k**2 + j**2 == i**2:
#                 coll.append([k, j, i])

# print(coll)
# print(len(coll))

# for item in coll:
#     if sum(item) == 1000:
#         print(item)
#         print(prod(item))

for a in range(1, 500):
    for b in range(1, a):
        c = (a**2+b**2)**0.5
        if a + b + c == 1000:
            print(a, b, c)
            print(a*b*c)