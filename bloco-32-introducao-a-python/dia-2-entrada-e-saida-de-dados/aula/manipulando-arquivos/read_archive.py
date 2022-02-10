# read all
# Aerys - Targaryan

# got_read = open("got_best_chars.txt", mode="r")
# content = got_read.read()
# print(content)
# got_read.close()

# result
# character - casa
# Jaime - Lannister
# Tyrion - Lannister
# Arya - Stark
# Hound - Clegane
# Jon - Snow
# Robert - Baratheon

# Read with iteraion
got_read = open("got_best_chars.txt", mode="r")
for line in got_read:
    print(line)
got_read.close()

# result
# character - casa

# Jaime - Lannister

# Tyrion - Lannister

# Arya - Stark

# Hound - Clegane

# Jon - Snow

# Robert - Baratheon

# Aerys - Targaryan
