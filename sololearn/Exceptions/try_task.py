# Вы создаете цифровое меню для заказа еды.

# Меню хранится в виде списка позиций.

# Ваша программа должна принимать индекс позиции в качестве ввода и выводить название позиции.

# Если индекс не действителен, вы должны выводить "Item not found".

# Если индекс действителен и название позиции успешно выводится, вы должны выводить "Thanks for your order".

menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']
#your code goes here

try:
    pos = int(input())
    print(menu[pos])
except IndexError:
    print("Item not found")
except ValueError:
    print("Item not found")
else:
    print("Thanks for your order")