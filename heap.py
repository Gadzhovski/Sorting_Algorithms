def heap_sorting(array):
    len_arr = len(array) - 1
    least = len_arr // 2
    for i in range(least, -1, -1):
        moving_down(array, i, len_arr)
    for i in range(len_arr, 0, -1):
        if array[0] > array[i]:
            replace(array, 0, i)
            moving_down(array, 0, i - 1)
    return array


def moving_down(array, first, last):
    biggest = 2 * first + 1
    while biggest <= last:
        if (biggest < last) and (array[biggest] < array[biggest + 1]):
            biggest += 1
        if array[biggest] > array[first]:
            replace(array, biggest, first)
            first = biggest
            biggest = 2 * first + 1
        else:
            return


def replace(arr, z, h):
    temporary = arr[z]
    arr[z] = arr[h]
    arr[h] = temporary
