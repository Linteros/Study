# Вы можете выбрасывать (или вызывать) исключения, когда происходит определенное условие.

# Например, когда вы получаете пользовательский ввод, который должен быть в определенном формате,
# вы можете выбросить исключение, если он не соответствует требованиям.

# Это делается с помощью оператора raise.

num = 102
if num > 100:
    raise ValueError

# Вам нужно указать type возникающего исключения.
# В приведенном выше коде мы вызываем ValueError.