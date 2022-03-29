# nums = [0, 10, 100, 1000]
nums1 = [1, 10]
nums2 = [10, 20]


class Conjuntos:
    def __init__(self):
        self.set = [False] * 1001
        self.last_element = 0

    def __str__(self):
        string = '{'

        for index, is_in_set in enumerate(self.set):
            if is_in_set:
                string += str(index)
                if index < self.last_element:
                    string += ", "

        string += '}'
        return string

    def __contains__(self, item):
        return self.set[item]

    def add(self, item):
        if item > 1000:
            return 'The param number must be inferior than 1000'

        if not self.set[item]:
            self.set[item] = True
        if item > self.last_element:
            self.last_element = item

    def union(self, conjuntoB):
        union = Conjuntos()
        for i, numb in enumerate(range(1001)):
            if self.set[i] or conjuntoB.set[i]:
                union.add(numb)

        return union

    def intersection(self, conjuntoB):
        intersec = Conjuntos()
        for i, numb in enumerate(range(1001)):
            if self.set[i] and conjuntoB.set[i]:
                intersec.add(numb)

        return intersec


def main():
    if __name__ == '__main__':
        conj1 = Conjuntos()
        conj2 = Conjuntos()

        for i in range(2):
            conj1.add(nums1[i])
            conj2.add(nums2[i])

    print(conj1.intersection(conj2))


main()
