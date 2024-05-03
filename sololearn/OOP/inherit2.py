# Класс, который наследуется от другого класса, называется подклассом.

# Класс, от которого происходит наследование, называется суперклассом.

# Если класс наследуется от другого с теми же атрибутами или методами, он их переопределяет.


class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")


class Dog(Wolf):
    def bark(self):
        print("Woof")


# В приведенном выше примере, Wolf является суперклассом, Dog является подклассом.

husky = Dog("Max", "grey")
husky.bark()