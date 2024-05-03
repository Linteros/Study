def my_max(arr):
    n = 0
    for i in arr:
        if i > n:
            n = i
    return n


def my_len(arr):
    if arr == []:
        return 0
    else:
        return 1 + my_len(arr[1:])


def my_max_rec(arr):
    if my_len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    elif my_len(arr) <= 1:
        return arr[0]
    sub_max = my_max_rec(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(my_max([234, 34, 3, 3, 6, 124, 34, 1234, 34, 3, 3, 1, 3]))
print(my_max_rec([234, 34, 3, 3, 6, 124, 34, 1234, 34, 3, 3, 1, 3]))