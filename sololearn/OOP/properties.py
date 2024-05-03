# Свойства позволяют настраивать доступ к атрибутам экземпляра.

# Они создаются путем размещения декоратора property над методом, что означает,
# что при доступе к атрибуту экземпляра с тем же именем, что и метод, будет вызван метод.

# Одним из распространенных применений свойства является создание read-only атрибута.


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True