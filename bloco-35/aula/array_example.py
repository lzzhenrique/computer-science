class Array:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def get(self, index):
        return self.data[index]

    def set(self, index, value):
        self.data.insert(index, value)

    def remove(self, index):
        self.data.pop(index)

    def update(self, index, value):
        self.remove(index)
        self.set(index, value)


# array = Array()
# array.set(0, 'Felipe')
# array.set(1, "Ana")
# array.set(2, "Shirley")
# array.set(3, "Miguel")
# print(array)

# array.update(3, 'Joana')
# print(array)

# array_memory_size = sys.getsizeof(array.data)
# print(array_memory_size)

# print(array.get(0))
# print(array.get(2))
