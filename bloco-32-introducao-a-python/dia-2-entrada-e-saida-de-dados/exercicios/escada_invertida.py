def word_ladder(word):
    for removed_letters in range(len(word)):
        for index in range(len(word) - removed_letters):
            print(word[index], end="")
        print()


name = input("Digite seu nome: ")
word_ladder(name)
