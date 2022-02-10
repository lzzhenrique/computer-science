# one

name = input("Say your name to me!!! ")

for char in name:
    print(char.upper())

# two
total = 0
numbers = input("what numbs sum? separe the values with space ")
for numb in numbers.split(" "):
    if (numb.isdigit()):
        total += int(numb)

print(total)
