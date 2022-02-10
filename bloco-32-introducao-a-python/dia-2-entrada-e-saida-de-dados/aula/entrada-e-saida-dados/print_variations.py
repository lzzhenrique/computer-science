from sys import stderr

print("Maria", "João", "Miguel", "Ana")  # saída: Maria João Miguel Ana
print("Maria", "João", "Miguel", "Ana", sep="?")
# saída: Maria, João, Miguel, Ana

X = 10
Y = 9
print(f"{X} / {Y} = {X / Y:.2f}")
print(f"{X:,}")

err = "System 32 corrompida"
print(f"Erro aconteceu: {err}", file=stderr)
