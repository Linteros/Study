def summa(arr):
    if arr == []:
        return 0
    return arr[0] + summa(arr[1:])


print(summa([3,6,2,56,3,4,5,6]))