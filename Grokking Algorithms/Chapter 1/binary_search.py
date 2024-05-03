def binary_search(list1, item):
    low = 0
    high = len(list1)-1

    # В переменных low и high хранятся границы
    # той части списка, в которой выполняется поиск

    while low <= high:
        mid = (low + high) // 2
        guess = list1[mid]

        # Пока эта часть не сократится до одного элемента
        # -- проверяем средний элемент

        if guess == item:
            return mid

        elif guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return None


my_list = range(0, 84567845845127396, 9)

print(binary_search(my_list, 126))
print(binary_search(my_list, -1))