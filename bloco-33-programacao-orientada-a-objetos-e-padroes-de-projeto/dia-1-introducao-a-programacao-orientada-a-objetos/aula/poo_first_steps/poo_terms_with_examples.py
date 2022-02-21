#  Entidade e classe são a mesma coisa, no caso User é a nossa entidade/classe.

# Uma classe tem metodos e atributos.
# Metodos: Coisas que a entidade/classe faz, uma funcao, por exemplo.
# __init__: É um metodo construtor, nele voce define os atribuitos iniciais.
# Atributos: Valores que a entidade/classe tem, ex: olhe as linhas 12 ate 14

# Instancia: É o uso da classe que voce criou, exemplos nas linhas 24 e 25
# Criando uma instancia, tu evoca o construtor da classe, e passa os params

# Objeto e instancia sao dois nomes para a mesma coisa.


# Pilares da POO
# Abstração = Crie entidades/classe
# Encapsulamento = Usar um metodo sem ter total dominio de como ele funciona

class football_coach:
    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        print("Envia email de reset da senha")


# instancias da classe **footbal_coach**
mourinho = football_coach("José Mourinho", "specialone@rome.com", "5pec1al0ne")
pep = football_coach("Josep Guardiola", "elpep@barça.com", "tikitaka")

# exemplo de uma mensagem ao objeto/instancia mourinho da linha 26
mourinho.reset_password()
