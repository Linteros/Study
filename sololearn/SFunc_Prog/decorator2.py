# Добавьте декоратор для системы выставления счетов, чтобы распечатать счет в требуемом формате


def decor(func):
    def zve(var):
        print('***')
        func(var)
        print('***')
        print('END OF PAGE')
    return zve


@decor
def invoice(num):
    print("INVOICE #" + num)


invoice(input())