# Магические методы - это специальные методы, которые имеют двойные подчеркивания в начале и в конце своих имен.

# Они также известны как dunders.

# До сих пор единственным, с которым мы столкнулись, является __init__, но есть и многие другие.

# Они используются для создания функциональности, которую нельзя представить обычным методом.

# Одно из обычных их применений - это перегрузка операторов.

# Это означает определение операторов для пользовательских классов,
# которые позволяют использовать на них такие операторы, как + и *.

# Пример магического метода - это __add__ для +.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

# Метод __add__ позволяет определить собственное поведение для оператора + в нашем классе.

# Как вы можете видеть, он складывает соответствующие атрибуты объектов
# и возвращает новый объект, содержащий результат.

# Как только он определен, мы можем складывать два объекта этого класса вместе.