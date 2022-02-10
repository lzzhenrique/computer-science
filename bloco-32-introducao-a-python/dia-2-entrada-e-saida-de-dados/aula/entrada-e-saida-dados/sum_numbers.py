# Input method naturaly returns a string, but this could be modified.
my_number = input("Digite seu numero ")
print(my_number)

# Above, input returns number
my_number = int(input("Digite seu numero "))
print(my_number)

# first while
my_number = 0
goal = 55

while my_number < goal:
    my_number += int(input("Pick a number: "))
    print("AAAAAAAAAAAAA")

print(f"A soma total passou de {goal}")
