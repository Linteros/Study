# Вы создаете приложение для рисования, в котором есть базовый класс Shape.

# Данный код определяет класс Rectangle, создает объект Rectangle и вызывает его методы area() и perimeter() .

# Сделайте следующее, чтобы завершить программу:

# 1. Унаследуйте класс Rectangle от Shape.

# 2. Определите метод perimeter() в классе Rectangle, печатая периметр прямоугольника.

# Периметр равен 2*(width+height)


class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width * self.height)


class Rectangle(Shape):
    # your code goes here
    def perimeter(self):
        print(2*(self.width+self.height))


w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()