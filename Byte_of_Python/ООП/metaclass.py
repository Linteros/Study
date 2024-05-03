# Точно так же, как классы используются для создания объектов, можно использовать метаклассы
# для создания классов. Метаклассы существуют для изменения или добавления
# нового поведения в классы.

# Давайте рассмотрим пример. Допустим, мы хотим быть уверены, что мы всегда создаём
# исключительно экземпляры подклассов класса SchoolMember, и не создаём экземпляры
# самого класса SchoolMember.

# Для достижения этой цели мы можем использовать концепцию под названием «абстрактные базовые классы».
# Это означает, что такой класс абстрактен, т.е. является лишь
# некой концепцией, не предназначенной для использования в качестве реального класса

# Мы можем объявить наш класс как абстрактный базовый класс при помощи встроенного
# метакласса по имени ABCMeta.

from abc import *


class SchoolMember(metaclass=ABCMeta):
    """Представляет любого человека в школе."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    @abstractmethod
    def tell(self):
        """Вывести информацию."""
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    """Представляет преподавателя."""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    """Представляет студента."""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()  # печатает пустую строку

members = [t, s]
for member in members:
    member.tell()  # работает как для преподавателя, так и для студента

# Мы можем объявить метод tell класса SchoolMember абстрактным, и таким образом
# автоматически запретим создавать экземпляры класса SchoolMember.
# Тем не менее мы можем работать с экземплярами Teacher и Student так, как будто они
# экземпляры SchoolMember, поскольку они являются подклассами.