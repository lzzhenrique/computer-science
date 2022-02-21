# Exercício 4:
# Mudando o nosso contexto para um sistema de vendas de uma cafeteria.
# Como podemos abstrair um pedido composto por vários itens?
# Quais seriam seu: nome, atributos e comportamentos?

# _____________________________________________________________________________________________________________
# Abstracao
# Item

# atributos/estados
# nome
# preco

# comportamentos
# alterar preco

# Abstracao
# Pedido

# cliente
# itens consumidos
# formas de pagamento
# descontos

# metodos
# calcular total
# calcular total com descontos

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def change_price(self, new_price):
        self.price = new_price


class Pedido:
    def __init__(self, client, itens, pay_way, discount):
        self.client = client
        self.itens = itens
        self.pay_way = pay_way
        self.discount = discount

    def total(self):
        total = 0
        for item in self.itens:
            total += float(item[1])
        return total

    def total_with_discount(self):
        total = self.total()
        total_discounted = total - ((self.discount * total) / 100)
        return total_discounted


menu = {
    "rosquinha": Item(name='rosquinha', price='2.00'),
    "pao de queijo": Item(name='pao de queijo', price='1.50'),
    "paozin": Item(name='paozin', price='1.00'),
    "bomba de chocolate": Item(name='bomba de chocolate', price='3.00'),
    "queijo": Item(name='queijo', price='5.00'),
    "leite": Item(name='leite', price='20.00'),
}

order = [
    (menu['bomba de chocolate'].name, menu['bomba de chocolate'].price),
    (menu['bomba de chocolate'].name, menu['bomba de chocolate'].price),
    (menu['bomba de chocolate'].name, menu['bomba de chocolate'].price),
    (menu['bomba de chocolate'].name, menu['bomba de chocolate'].price),
    (menu['bomba de chocolate'].name, menu['bomba de chocolate'].price),
    (menu['bomba de chocolate'].name, menu['bomba de chocolate'].price),
    (menu['bomba de chocolate'].name, menu['bomba de chocolate'].price),
    (menu['bomba de chocolate'].name, menu['bomba de chocolate'].price),
]
cliente = "James"
payment = "credit card"
desc = 5

pedido1 = Pedido(client=cliente, pay_way=payment, discount=desc, itens=order)
print(pedido1.itens)
print(pedido1.total())
print(pedido1.total_with_discount())
