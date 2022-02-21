# all

negative = [1, 2, None, 3, 4, "a"]
positive = [1, 2, 3, 4, "a"]


# print(all(positive))

# any
variable1 = [{None}, {"CR7"}, {"Messi"}]

# print(any(variable1))

# sum

over_million = sum([10, 40, 55, 88, 2], start=1657423)
# print(over_million)

# enumerate
teclado = enumerate(["a", "b", "c", "d", "e", "f", "g", "h", "i"])

for elem, value in teclado:
    print(f"({elem}, {value})")
