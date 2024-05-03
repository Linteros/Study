#  Наследование позволяет делиться функциональностью между классами.

# Представьте несколько классов, Cat, Dog, Rabbit и так далее.
# Несмотря на то, что они могут отличаться по некоторым параметрам (только у Dog может быть метод bark),
# они, вероятно, будут схожи по другим (все имеют атрибуты color и name).

# Это сходство можно выразить, заставив их всех наследовать от суперкласса Animal,
# который содержит общую функциональность.

# Чтобы унаследовать класс от другого класса, укажите имя суперкласса в скобках после имени класса.


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()