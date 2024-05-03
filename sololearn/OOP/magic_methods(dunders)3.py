# Python также предоставляет магические методы для сравнений.

# __lt__ для <
# __le__ для <=
# __eq__ для ==
# __ne__ для !=
# __gt__ для >
# __ge__ для >=

#  Если __ne__ не реализован, он возвращает противоположность __eq__.
# Нет других связей между другими операторами.

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

# Как вы можете видеть, вы можете определить любое пользовательское поведение для перегруженных операторов.