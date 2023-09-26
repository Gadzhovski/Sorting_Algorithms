def insertion_sorting(lst):
    for ind in range(1, len(lst)):
        present = lst[ind]
        place = ind
        while place > 0 and lst[place-1] > present:
            lst[place] = lst[place-1]
            place -= 1
        lst[place] = present
    return lst
