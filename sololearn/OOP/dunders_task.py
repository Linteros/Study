# Мы улучшаем наше приложение для рисования.

# На нашем приложении должна быть возможность добавления и сравнения двух объектов типа Shape.

# Добавьте соответствующие методы для включения операции сложения + и сравнения
# с использованием оператора больше > для класса Shape.

# Сложение должно возвращать новый объект с суммой ширин и высот операндов,
# в то время как сравнение должно возвращать результат сравнения площадей объектов.

# Данный код создает два объекта Shape из пользовательского ввода, выводит area() их сложения и сравнивает их.


class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    # your code goes here
    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)

    def __gt__(self, other):
        return self.area() > other.area()


w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)