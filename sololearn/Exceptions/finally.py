# После оператора try/except может следовать блок finally
# Он будет выполняться после блока try/except, независимо от того, произошло исключение или нет.

try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

# finally блок полезен, например, при работе с файлами и ресурсами:
# его можно использовать для того, чтобы убедиться, что файлы или ресурсы
# закрыты или освобождены, независимо от того, произошло ли исключение.