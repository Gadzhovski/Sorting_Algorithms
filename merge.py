def merge(left_array, right_array):
    new_list = []
    while len(left_array) != 0 and len(right_array) != 0:
        if left_array[0] < right_array[0]:
            new_list.append(left_array[0])
            left_array.remove(left_array[0])
        else:
            new_list.append(right_array[0])
            right_array.remove(right_array[0])
    if len(left_array) == 0:
        new_list += right_array
    else:
        new_list += left_array
    return new_list


def merge_sorting(lst):
    if len(lst) < 2:
        return lst
    else:
        middle = len(lst) // 2
        left_array = merge_sorting(lst[:middle])
        right_array = merge_sorting(lst[middle:])
        return merge(left_array, right_array)
