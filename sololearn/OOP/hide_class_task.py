# Мы работаем над игрой. Наш класс Player имеет атрибуты name и приватные _lives.

# Метод hit() должен уменьшать количество жизней игрока на 1.
# В случае, если количество жизней равно 0, он должен выводить "Game Over".

# Завершите метод hit(), чтобы программа работала как ожидалось.

# Код создает объект Player и вызывает его метод hit() несколько раз.


class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
        if self._lives == 0:
            print('Game Over')


p = Player("Cyberpunk77", 3)
p.hit()
p.hit()
p.hit()