# Исключения возникают тогда, когда в программе возникает некоторая исключительная
# ситуация. Например, к чему приведёт попытка чтения несуществующего файла? Или
# если файл был случайно удалён, пока программа работала? Такие ситуации обрабатываются при помощи исключений.
# Это касается и программ, содержащих недействительные команды. В этом случае Python
# поднимает руки и сообщает, что обнаружил ошибку

# Обрабатывать исключения можно при помощи оператора try..except
# При этом все обычные команды помещаются внутрь try-блока,
# а все обработчики исключений – в except-блок

try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))

# Здесь мы поместили все команды, которые могут вызвать исключения/ошибки, внутрь блока try,
# а затем поместили обработчики соответствующих ошибок/исключений в блок except.
# Выражение except может обрабатывать как одиночную ошибку или исключение,
# так и список ошибок/исключений в скобках. Если не указано имя ошибки или исключения,
# обрабатываться будут все ошибки и исключения.