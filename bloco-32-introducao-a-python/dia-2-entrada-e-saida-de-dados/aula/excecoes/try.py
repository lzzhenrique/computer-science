# while True:
#   try:
#      x = int(input("Please enter a number: "))
#     break
# except ValueError:
#   print("Oops!  That was no valid number.  Try again...")

#try:
#    arquivo = open("arquivo.txt", "w")
# except OSError:
#    print("inexistent archive")
# else:
#    print("arquivo manipulado e fechado com sucesso")
#    arquivo.close()
# finally:
#    print("Tentativa de abrir o archive")

with open("arquivo.txt", "w") as file:
    file.write('Michelle 27\n')

print(file.closed)