A = []


class User:
    def __init__(self, name, email, password):
        A.append(self)

        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        print("Envia email pedindo mudanca de senha!")


new_user = User("José Mourinho", "specialone@rome.com", "5pec1al0ne")

for elem in A:
    print(elem.name)
    print(new_user.name)
    print(elem == new_user)


# levar pra mentoria
# Self é adicionado ao array A antes de ter os valores atribuidos, mas ainda assim, nos consoles da linha 17 e 20, ele retorna o nome.