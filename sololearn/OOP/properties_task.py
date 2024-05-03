# Мы улучшаем нашу игру и нам нужно добавить свойство isAlive, которое возвращает True,
# если количество жизней больше 0.

# Дополните код, добавив свойство isAlive.

# Код использует цикл while для нанесения ударов Player,
# пока количество его жизней не станет равным 0, используя свойство isAlive для создания условия.


class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1

    # your code goes here
    @property
    def isAlive(self):
        if self._lives > 0:
            return True
        else:
            return False


p = Player("Cyberpunk77", int(input()))
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break