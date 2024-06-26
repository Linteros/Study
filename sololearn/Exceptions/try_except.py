# Когда происходит исключение, программа прекращает выполнение.

# Чтобы обработать исключения и вызвать код при возникновении исключения,
# вы можете использовать оператор try/except.

# Блок try содержит код, который может вызвать исключение. Если это исключение происходит,
# код в блоке try прекращает выполнение, и выполняется код в блоке except.
# Если ошибки не произошло, код в блоке except не выполняется.

try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

# Поскольку код вызывает исключение ZeroDivisionError, выполняется код в блоке except.

# В приведенном выше коде, оператор except определяет тип обрабатываемого исключения
# (в нашем случае, ZeroDivisionError).