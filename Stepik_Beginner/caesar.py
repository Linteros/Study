en_low = 'abcdefghijklmnopqrstuvwxyz'
en_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
rus_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

x = int(input())  # 1 - шифр, 0 - де шифр
language = input()
rot_n = int(input())
text = input()


def func_s(s, lang_up, lang_low, tx):
    res = ''
    for i in tx:
        if i in lang_up:
            if lang_up.index(i) + s < len(lang_up):
                res += lang_up[lang_up.index(i) + s]
            else:
                res += lang_up[lang_up.index(i) - len(lang_up) + s]
        elif i in lang_low:
            if lang_low.index(i) + s < len(lang_low):
                res += lang_low[lang_low.index(i) + s]
            else:
                res += lang_low[lang_low.index(i) - len(lang_low) + s]
        else:
            res += i
    return res


def func_ds(s, lang_up, lang_low, tx):
    res = ''
    for i in tx:
        if i in lang_up:
            res += lang_up[lang_up.index(i) - s]
        elif i in lang_low:
            res += lang_low[lang_low.index(i) - s]
        else:
            res += i
    return res


if x == 1:
    if language == 'en':
        print(func_s(rot_n, en_up, en_low, text))
    elif language == 'ru':
        print(func_s(rot_n, rus_up, rus_low, text))
elif x == 0:
    if language == 'en':
        print(func_ds(rot_n, en_up, en_low, text))
    elif language == 'ru':
        print(func_ds(rot_n, rus_up, rus_low, text))


def all_results():
    for i in range(1, 25+1):
        print(func_ds(i, en_up, en_low, text), i)


all_results()