# Центральным элементом Объектно-ориентированного программирования (OOP) являются объекты,
# которые создаются с использованием классов.

# Класс описывает, что будет объект, но отдельно от самого объекта.
# Другими словами, класс можно описать как чертеж, описание или определение объекта.

# Вы можете использовать один и тот же класс в качестве чертежа для создания нескольких разных объектов.

# Классы создаются с использованием ключевого слова class и отступа,
# который содержит методы класса (функции класса).

# Ниже приведен пример простого класса и его объектов.


class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)


# Этот код определяет класс под названием Cat, у которого есть два атрибута: color и legs.

# Затем класс используется для создания 3 отдельных объектов этого класса.