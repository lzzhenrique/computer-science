estudantes = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
lista1_entregues = set(['a', 'd', 'g', 'c'])
lista2_entregues = set(['c', 'a', 'f'])


# Quem ainda nao entregou a lista 1?
print(estudantes.difference(lista1_entregues))

# Quem já entregou as duas listas?
print(estudantes.intersection(lista1_entregues, lista2_entregues))

# Quem já entregou qualquer uma das duas listas?
print(lista1_entregues.union(lista2_entregues))

# Quem ainda não entregou nenhuma das listas?
print(estudantes.difference(lista1_entregues, lista2_entregues))
