file = open("arquivo.dat", mode="wb")
file.write(b"C\xc3\xa1ssio 30")
file.close()

file = open("arquivo.dat", mode="rb")
content = file.read()
print(content)
file.close()
