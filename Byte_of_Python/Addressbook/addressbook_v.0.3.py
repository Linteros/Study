import pickle

ADDRESS_BOOK_FILE = "addressbook.data"


class AddressBook:
    def __init__(self):
        # Создание пустого словаря для хранения адресов
        self.addresses = {}

    def start(self):
        try:
            print("\nАдресная книга \"Vlad\'os first project\"\n"
                  "Для продолжения выберите одно из действий:\n"
                  "Search \"name\"- найти данные\n"
                  "Save \"name\"- записать новые данные или изменить старые\n"
                  "Del \"name\"- удалить данные\n"
                  "All - вывести всю Адресную книгу\n"
                  "Для выхода из программы введите \"quit\"\n")

            with open(ADDRESS_BOOK_FILE, "rb") as f:
                # Загрузка адресов из файла
                self.addresses = pickle.load(f)

            # Получение действия и имени от пользователя
            action = input("Ввод: ").split()

            if len(action) < 2:
                if action[0] == "All":
                    self.all()
                else:
                    raise ValueError

            if action[0] == "Search":
                self.search(action[1])
            elif action[0] == "Save":
                self.save(action[1])
            elif action[0] == "Del":
                self.delete(action[1])
            elif action[0] == "All":
                self.all()
            elif action[0] == "quit":
                print("До встречи!")
        except ValueError:
            print("\nВведите корректное количество аргументов")
            self.cont()
        except Exception as e:
            print(f"\nУпс, что-то пошло не так... {e}")

    def cont(self):
        # Предлагает пользователю продолжить или завершить программу
        response = input("\nЕсли хотите продолжить - введите \"Yes\"\nЧтобы выйти - введите любой символ\n\nВвод: ")
        if response == "Yes":
            self.start()
        else:
            print("\nДо встречи!")

    def all(self):
        try:
            print("")
            # Вывод всех адресов
            for key, value in self.addresses.items():
                print(f"{key}: {value}")
            print("\nВыгрузка завершена!")
            self.cont()
        except (EOFError, FileNotFoundError):
            print("\nАдресная книга пуста, но вы можете это исправить!")
            self.cont()
        except Exception as e:
            print(f"\nУпс, что-то пошло не так... {e}")
            self.cont()

    def delete(self, name):
        try:
            if name in self.addresses:
                # Удаление адреса из адресной книги
                del self.addresses[name]
                with open(ADDRESS_BOOK_FILE, "wb") as f:
                    pickle.dump(self.addresses, f)
                print(f"\nУдаление {name} из адресной книги...")
            else:
                print(f"\n{name} ещё нет в адресной книге, но вы можете это исправить!")
            self.cont()
        except (EOFError, FileNotFoundError):
            print("\nАдресная книга пуста, но вы можете это исправить!")
            self.cont()
        except Exception as e:
            print(f"\nУпс, что-то пошло не так... {e}")
            self.cont()

    def save(self, name):
        try:
            if name in self.addresses:
                print(f"\n{name} уже есть в адресной книге")
                if input("Хотите изменить данные? (Yes/No): ").lower() == "yes":
                    # Изменение адреса
                    address = input("\nВведите новый адрес: ")
                    self.addresses[name] = address
            else:
                # Добавление нового адреса
                address = input("\nВведите адрес: ")
                self.addresses[name] = address

            with open(ADDRESS_BOOK_FILE, "wb") as f:
                # Сохранение адресов в файл
                pickle.dump(self.addresses, f)
                print(f"\nДанные {name} добавлены в адресную книгу!")
            self.cont()
        except Exception as e:
            print(f"\nУпс, что-то пошло не так... {e}")
            self.cont()

    def search(self, name):
        try:
            if name in self.addresses:
                # Поиск адреса по имени
                print("\nДанные успешно найдены!\n")
                print(self.addresses[name], "\n")
            else:
                print(f"{name} ещё нет в адресной книге, но вы можете это исправить!")
            self.cont()
        except (EOFError, FileNotFoundError):
            print("\nАдресная книга пуста, но вы можете это исправить!")
            self.cont()
        except Exception as e:
            print(f"\nУпс, что-то пошло не так... {e}")
            self.cont()


if __name__ == "__main__":
    # Создание экземпляра класса AddressBook и вызов метода start()
    address_book = AddressBook()
    address_book.start()