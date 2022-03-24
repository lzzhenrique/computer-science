def bubble_sort(array):
    has_swapped = True

    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        range_var = range(len(array) - num_of_iterations - 1)
        for i in range_var:
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
        num_of_iterations += 1

    return array


print(bubble_sort([100, 4, 6, 33, 56, 67]))
