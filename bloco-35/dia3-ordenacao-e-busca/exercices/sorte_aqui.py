def find_pivot(list, inicio, last_position):
    pivot = list[last_position]
    pivot_pos = inicio
    range_list = range(inicio, last_position)

    for curr_pos in range_list:
        if list[curr_pos] <= pivot:
            list[curr_pos], list[pivot_pos] = list[pivot_pos], list[curr_pos]
            pivot_pos += 1

    list[last_position], list[pivot_pos] = list[pivot_pos], list[last_position]

    return pivot_pos


def quick_sort(list1, inicio=0, fim=None):
    if fim is None:
        fim = len(list1) - 1

    if inicio < fim:
        pivot_position = find_pivot(list1, inicio, fim)
        quick_sort(list1, inicio, pivot_position - 1)
        quick_sort(list1, pivot_position + 1, fim)


# quick_sort(my_list)
# print(my_list)
