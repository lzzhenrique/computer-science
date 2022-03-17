from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str

    def func(self):
        return print('mahoe')


teclado = Pessoa("paulo")
teclado.func()
