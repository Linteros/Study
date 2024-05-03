# Вы можете использовать встроенную функцию dir, чтобы получить список идентификаторов,
# которые объект определяет. Так в число идентификаторов модуля входят функции,
# классы и переменные, определённые в этом модуле

# Выполнять в консоли

import sys # получим список атрибутов модуля 'sys'

dir(sys)

dir() # получим список атрибутов текущего модуля

a = 5  # создадим новую переменную 'a'

dir()

del a # удалим имя 'a'

dir()