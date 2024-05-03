# Больше магических методов для общих операторов:

# __sub__ для -
# __mul__ для *
# __truediv__ для /
# __floordiv__ для //
# __mod__ для %
# __pow__ для **
# __and__ для &
# __xor__ для ^
# __or__ для |

# Выражение x + y преобразуется в x.__add__(y).

# Однако, если x не реализовал __add__, и x и y разного типа, тогда вызывается y.__radd__(x).

# Существуют эквивалентные r методы для всех только что упомянутых магических методов.

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

# В приведенном выше примере мы определили операцию деления для нашего класса SpecialString.