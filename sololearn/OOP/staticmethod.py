# Статические методы похожи на методы класса, за исключением того, что они не получают
# никаких дополнительных аргументов; они идентичны обычным функциям, которые принадлежат классу.

# Они отмечены декоратором staticmethod.


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True


ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

# Статические методы ведут себя как обычные функции, за исключением того,
# что вы можете вызывать их из экземпляра класса.