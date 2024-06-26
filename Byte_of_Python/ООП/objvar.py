# Существует два типа полей: переменные класса и переменные объекта, которые различаются
# в зависимости от того, принадлежит ли переменная классу или объекту соответственно.

# Переменные класса разделяемы – доступ к ним могут получать все экземпляры этого класса.
# Переменная класса существует только одна, поэтому когда любой из объектов изменяет переменную класса,
# это изменение отразится и во всех остальных экземплярах того же класса

# Переменные объекта принадлежат каждому отдельному экземпляру класса. В этом случае
# у каждого объекта есть своя собственная копия поля, т.е.
# не разделяемая и никоим образом не связанная с другими такими же полями в других экземплярах


class Robot:
    """Представляет робота с именем."""
# Переменная класса, содержащая количество роботов
    population = 0

    def __init__(self, name):
        """Инициализация данных."""
        self.name = name
        print('(Инициализация {0})'.format(self.name))

        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population += 1

    def __del__(self):
        """Я умираю."""
        print('{0} уничтожается!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))

    def sayHi(self):
        """Приветствие робота.

        Да, они это могут."""
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))

    def howMany():
        """Выводит численность роботов."""

        print('У нас {0:d} роботов.'.format(Robot.population))

    howMany = staticmethod(howMany)


droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2

Robot.howMany()


# Здесь population принадлежит классу Robot, и поэтому является переменной класса.
# Переменная name принадлежит объекту (ей присваивается значение при помощи self),
# и поэтому является переменной объекта

# Таким образом, мы обращаемся к переменной класса population как
# Robot.population, а не self.population. К переменной же объекта name
# во всех методах этого объекта мы обращаемся при помощи обозначения
# self.name. Помните об этой простой разнице между переменными класса и
# объекта. Также имейте в виду, что переменная объекта с тем же именем, что
# и переменная класса, сделает недоступной («спрячет») переменную класса!

# Метод howMany принадлежит классу, а не объекту. Это означает, что мы можем определить
# его как classmethod или staticmethod, в зависимости от того,
# нужно ли нам знать, в каком классе мы находимся. Поскольку нам не нужна такая информация,
# мы воспользуемся staticmethod.

# Мы могли достичь того же самого, используя декораторы:

# @staticmethod
# def howMany():
#   '''Выводит численность роботов.'''
#   print('У нас {0:d} роботов.'.format(Robot.population))