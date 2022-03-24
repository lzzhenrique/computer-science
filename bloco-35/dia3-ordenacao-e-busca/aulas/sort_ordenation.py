def insertion_sort(array):
    for index in range(len(array)):
        current_value = array[index]
        current_position = index
        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
            array[current_position] = current_value
            print(index)
    return array


print(insertion_sort([100, 4, 6, 33, 56, 7, 67]))
