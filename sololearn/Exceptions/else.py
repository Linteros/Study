# Оператор else также может использоваться с операторами try/except.

# В этом случае, код, находящийся в нем, выполнится только в том случае,
# если в операторе try не произошло ошибки.

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)