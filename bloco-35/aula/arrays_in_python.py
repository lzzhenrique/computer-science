import sys
from array import array

my_array = array('I')

my_array.insert(0, 5)
my_array.insert(1, 3)
my_array.insert(2, 5)

print("Após adicionar alguns valores: ", my_array)


my_array.insert(1, 4)

print("Após inserção em índice intermediário: ", my_array)


elements = list(range(100))  # definimos uma lista de 100 números
print("Tamanho da lista:", sys.getsizeof(elements))
array_from_list = array("I", elements)  # criamos um array a partir da lista
print("Tamanho do array", sys.getsizeof(array_from_list))