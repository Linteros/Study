# У классов могут быть определены другие методы для добавления функциональности.

# Помните, что все методы должны иметь self в качестве своего первого параметра.

# Доступ к этим методам осуществляется с использованием того же точечного синтаксиса, что и для атрибутов


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()
