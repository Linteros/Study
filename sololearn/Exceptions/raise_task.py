# Вы создаете программу для публикации твитов. Каждый твит не должен превышать 42 символа.

# Дополните программу, чтобы вызывать исключение, в случае, если длина твита превышает 42 символа.

tweet = input()

try:
# your code goes here
    if len(tweet) > 42:
        raise ValueError
except:
    print("Error")
else:
    print("Posted")