arquivos = []

for index in range(10240):
    arquivos.append(open(f"arquivo {index}.txt", "w"))

# fails in 8161 archive
