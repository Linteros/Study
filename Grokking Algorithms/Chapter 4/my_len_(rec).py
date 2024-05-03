def my_len(arr):
    if arr == []:
        return 0
    else:
        return 1 + my_len(arr[1:])


print(my_len([2,5,4,3,6,5,3,43,43,43]))