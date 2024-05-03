# Оператор try может иметь несколько различных блоков except для обработки различных исключений.

# Несколько исключений также могут быть помещены в один блок except с использованием скобок,
# чтобы блок except обрабатывал все они.

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")

# Вы можете обрабатывать столько исключений в выражении except, сколько вам нужно.