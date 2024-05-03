# Создайте собственную программу «Адресная книга», работающую из командной строки
# и позволяющую просматривать, добавлять, изменять, удалять или искать контактные
# данные ваших знакомых. Кроме того, эта информация также должна сохраняться на диске для последующего доступа.

import pickle

ABfile = "addressbook.data"
AB = {}
address = None


class AddressBook:

    def __init__(self, name):

        self.name = name

    @staticmethod
    def start():

        try:
            print("""\nАдресная книга \"Vlad\'os first project\"\n
Для продолжения выберите одно из действий:\n
Search \"name\"- найти данные
Save \"name\"- записать новые данные или изменить старые
Del \"name\"- удалить данные
All - вывести всю Адресную книгу\n
Для выхода из программы введите любой символ\n
Ввод: """, end="")
            word, name = input().split()

            if word == "Search":
                AddressBook.search(name)

            elif word == "Save":
                AddressBook.save(name)

            elif word == "Del":
                AddressBook.delete(name)

            elif word == "All":
                AddressBook.all()

            else:
                print("До встречи!")

        except ValueError:
            AddressBook.all()

    @staticmethod
    def cont():

        print("""\nЕсли хотите продолжить - введите \"Yes\"
Чтобы выйти - введите любой символ\n
Ввод: """, end="")
        word = input()
        AddressBook.check(word)

    @staticmethod
    def check(word):

        if word == "Yes":
            AddressBook.start()
        else:
            print("\nДо встречи!")

    @staticmethod
    def all():

        global f

        try:
            f = open(ABfile, "rb")
            AB = pickle.load(f)
            f.close()
            print("\n")

            for key in AB:
                print(f"{key}: ", AB[f"{key}"])
            print("\nВыгрузка завершена!")
            AddressBook.cont()

        except EOFError:
            f.close()
            print("\nАдресная книга пуста, но вы можете это исправить!")
            AddressBook.cont()

        except FileNotFoundError:
            f = open(ABfile, "wb")
            f.close()
            print("""Ой, у нас не было адресной книги, но мы всё починили!\n
Пожалуйста, начните сначала""")
            AddressBook.start()

        except:
            f.close()
            print("\nУпс, что-то пошло не так...")
            AddressBook.cont()


    @staticmethod
    def delete(name):

        global f

        try:
            f = open(ABfile, "rb")
            AB = pickle.load(f)
            f.close()
            f = open(ABfile, "wb")
            AB.pop(f"{name}")
            print(f"\nУдаление {name} из адресной книги...\n")
            pickle.dump(AB, f)
            f.close()
            print(f"Удаление {name} завершено!")
            AddressBook.cont()

        except KeyError:
            f.close()
            print(f"\n{name} ещё нет в адресной книге, но вы можете это исправить!")
            AddressBook.cont()

        except EOFError:
            f.close()
            print("\nАдресная книга пуста, но вы можете это исправить!")
            AddressBook.cont()

        except FileNotFoundError:
            f = open(ABfile, "wb")
            f.close()
            print("""Ой, у нас не было адресной книги, но мы всё починили!\n
        Пожалуйста, начните сначала""")
            AddressBook.start()

        except:
            f.close()
            print("\nУпс, что-то пошло не так...")
            AddressBook.cont()

    @staticmethod
    def save(name):
        """Функция добавляет Имя и Адрес
        Если Имя уже существует, то изменяет Адрес"""
        global f
        try:

            # Здесь подгружается словарь из файла

            f = open(ABfile, "rb")
            AB = pickle.load(f)
            f.close()

            if f"{name}" in AB:
                print(f"""{name} уже есть в адресной книге\n
Если вы хотите изменить данные {name}: напишите \"Yes\"
В ином случае введите любой символ\n
Ввод: """, end="")
                n = input()

                if n == "Yes":
                    f = open(ABfile, "wb")
                    print("\nВведите данные:", end=" ")
                    address = input()
                    AB[f"{name}"] = address
                    pickle.dump(AB, f)
                    f.close()
                    print(f"\nДанные {name} добавлены в адресную книгу!")
                    AddressBook.cont()

                else:
                    AddressBook.cont()

            # Это тело нормального выполнения функции

            f = open(ABfile, "wb")
            print("\nВведите данные:", end=" ")
            address = input()
            AB[f"{name}"] = address
            pickle.dump(AB, f)
            f.close()
            print(f"\nДанные {name} добавлены в адресную книгу!")
            AddressBook.cont()

        except EOFError:

            # Случай, если адресная книга пустая

            AB = {}
            print("\nУх ты, вы первый, кто заполняет эту книгу!\n")
            f = open(ABfile, "wb")
            print("Введите данные:", end=" ")
            address = input()
            AB[f"{name}"] = address
            pickle.dump(AB, f)
            f.close()
            print(f"Данные {name} добавлены в адресную книгу!")
            AddressBook.cont()

        except FileNotFoundError:
            f = open(ABfile, "wb")
            f.close()
            print("""Ой, у нас не было адресной книги, но мы всё починили!\n
        Пожалуйста, начните сначала""")
            AddressBook.start()

        except:
            f.close()
            print("\nУпс, что-то пошло не так...")
            AddressBook.cont()

    @staticmethod
    def search(name):
        global f
        try:
            f = open(ABfile, "rb")
            AB = pickle.load(f)
            f.close()
            if f"{name}" in AB:
                print("Данные успешно найдены!\n")
                print(AB[f"{name}"],"\n")
                AddressBook.cont()
            else:
                print(f"{name} ещё нет в адресной книге, но вы можете это исправить!")
                AddressBook.cont()
        except EOFError:
            f.close()
            print("\nАдресная книга пуста, но вы можете это исправить!")
            AddressBook.cont()

        except FileNotFoundError:
            f = open(ABfile, "wb")
            f.close()
            print("""Ой, у нас не было адресной книги, но мы всё починили!\n
        Пожалуйста, начните сначала""")
            AddressBook.start()
            
        except:
            f.close()
            print("\nУпс, что-то пошло не так...")
            AddressBook.cont()


AddressBook.start()