got_file = open("got_best_chars.txt", mode="w")

got_file.write("character - casa\n")
got_file.write("Jaime - Lannister\n")
got_file.write("Tyrion - Lannister\n")
got_file.write("Arya - Stark\n")

print("Hound - Clegane", file=got_file)

OTHER_CHARS = ["Jon - Snow\n", "Robert - Baratheon\n" "Aerys - Targaryan"]

got_file.writelines(OTHER_CHARS)

got_file.close()