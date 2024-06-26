# Банкомат принимает сумму для снятия в качестве входного значения и вызывает соответствующий метод снятия.

# Если входное значение не является числом, машина должна выводить "Please enter a number".

# Используйте обработку исключений для ввода числа, вызова метода withdraw()
# с введенным значением в качестве аргумента, и вывода "Please enter a number",
# в случае, если входное значение не является числом.

# ValueError возникает, когда вы пытаетесь преобразовать нецелое число в целое с помощью int().


def withdraw(amount):
    print(str(amount) + " withdrawn!")

# your code goes here


try:
    withdraw(int(input()))
except ValueError:
    print('Please enter a number')