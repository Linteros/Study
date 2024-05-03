# Существует несколько магических методов для создания классов, которые действуют как контейнеры.

# __len__ для len()
# __getitem__ для индексации
# __setitem__ для присваивания индексированным значениям
# __delitem__ для удаления индексированных значений
# __iter__ для итерации по объектам (например, в циклах for)
# __contains__ для in

# Есть много других магических методов, которые мы здесь не рассматриваем,
# таких как __call__ для вызова объектов как функций, и __int__, __str__, и подобных,
# для преобразования объектов во встроенные типы.

import random


class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)


vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

# Мы переопределили функцию len() для класса VagueList, чтобы она возвращала случайное число.

# Функция индексации также возвращает случайный элемент из диапазона списка, основываясь на выражении