# Вы создаете видеоигру! В данном коде объявляется класс Player, с его атрибутами и методом intro().
#
# Дополните код так, чтобы он принимал имя и уровень от пользователя, создавал объект
# Player с соответствующими значениями и вызывал метод intro() этого объекта.
#
# Пример ввода:
# Tony
# 12
#
# Пример вывода:
# Tony (Уровень 12)
#
# Используйте синтаксис с точкой для вызова метода intro() для объявленного объекта.


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")


# your code goes here

player = Player(input(), input())
player.intro()