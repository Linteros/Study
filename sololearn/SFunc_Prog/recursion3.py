# Исправьте код так, чтобы он мог преобразовывать свой аргумент из десятичного в двоичный

def convert(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num % 2 + 10 * convert(num // 2)


print(convert(int(input())))