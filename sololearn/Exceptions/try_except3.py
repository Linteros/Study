# Оператор except без указания конкретного исключения будет перехватывать все ошибки.
# Такие операторы следует использовать с осторожностью,
# поскольку они могут перехватывать неожиданные ошибки и скрывать ошибки программирования.

try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")

# Обработка исключений особенно полезна при работе с пользовательским вводом.