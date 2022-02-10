from random import randint

random_number = randint(1, 10)
guess = ""

while guess != random_number:
    guess = int(input("Qual o seu palpite? "))

print(f"O numero sorteado era: {guess}")
