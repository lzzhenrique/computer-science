entrada = [1, 3, 2, 4, 5, 1]


def find_duplicate(array):
    conjunto = set(array)

    for numb in array:
        if numb in conjunto:
            conjunto.discard(numb)
        else:
            return numb


print(find_duplicate(entrada))
