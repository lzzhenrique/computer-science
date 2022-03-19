
# Em um conjunto de números desordenados, crie uma função para ordena-los.
my_list = [3, 24, 14, 25, 10, 9, 22, 15, 0, 2, 11, 13, 23, 4, 18, 8, 5, 29]


def find_pivot(list, start, last_pos):
    pivot = list[last_pos]
    pivot_pos = start

    for curr_pos in range(start, last_pos):
        if list[curr_pos] <= pivot:
            list[pivot_pos], list[curr_pos] = list[curr_pos], list[pivot_pos]
            pivot_pos += 1

    list[pivot_pos], list[last_pos] = list[last_pos], list[pivot_pos]

    return pivot_pos


def quick_sort(list, start=0, end=None):
    if end is None:
        end = len(list) - 1

    if start < end:
        pivot_position = find_pivot(list, start, end)
        quick_sort(list, start, pivot_position - 1)
        quick_sort(list, pivot_position + 1, end)


quick_sort(my_list)
print(my_list)
