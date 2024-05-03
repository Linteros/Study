# Данный код принимает 2 числа в качестве входных данных и вызывает статический метод area()
# класса Shape, чтобы вывести площадь фигуры, которая равна высоте, умноженной на ширину.

# Чтобы код работал, вам нужно определить класс Shape и статический метод area(),
# который должен возвращать произведение своих двух аргументов.

# Используйте декоратор @staticmethod для определения статического метода

# your code goes here


class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    @staticmethod
    def area(width, height):
        return width * height


w = int(input())
h = int(input())

print(Shape.area(w, h))