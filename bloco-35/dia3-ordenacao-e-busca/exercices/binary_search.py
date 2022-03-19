my_list = [0, 1, 2, 2, 2, 4, 4, 5, 6, 7, 7, 8, 9, 11, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 21, 22, 23, 23, 26, 27, 28, 29, 30, 41, 998]

# VERSAO 1
# 20 operacoes para achar o valor 30
# A principio, essa versao requere menos steps que a V 2.

# def binary_search(list, value_to_find):
#     middle = len(list) // 2

#     if list[middle] < value_to_find:
#         return binary_search(list[middle:], value_to_find)

#     if list[middle] > value_to_find:
#         return binary_search(list[:middle], value_to_find)

#     if list[middle] == value_to_find:
#         return list[middle]

#     return 'Valor nao encontrado na lista existente'


# print(binary_search(my_list, 30))


# VERSAO 2
# 20 operacoes para achar o valor 30
# A principio, essa versao requere mais steps que a V1.

# def binary_search(list, value_to_find):
#     middle = len(list) // 2
#     middle_left = middle - 1
#     middle_right = middle + 1

#     if list[middle_left] == value_to_find:
#         return list[middle_left]

#     if list[middle_right] == value_to_find:
#         return list[middle_right]

#     if list[middle] < value_to_find:
#         return binary_search(list[middle:], value_to_find)

#     if list[middle] > value_to_find:
#         return binary_search(list[:middle], value_to_find)

#     return 'Valor nao existente na lista enviada'


# print(binary_search(my_list, 30))


# Versao 3, do video.


def binary_search(array, item, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start <= end:
        middle = (start + end) // 2

        if array[middle] == item:
            return middle, array[middle]
        if item < array[middle]:
            return binary_search(array, item, start, middle - 1)
        else:
            return binary_search(array, item, middle + 1, end)

    return None


print(binary_search(my_list, 27))
