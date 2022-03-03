from collections.abc import Iterator, Iterable


class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)


class IteradorDoBaralho(Iterator):
    def __init__(self, cartas):
        self._cartas = cartas
        self._pos = 0

    def __next__(self):
        try:
            carta = self._cartas[self._pos]
        except IndexError:
            raise StopIteration()
        else:
            self._pos += 1
            return carta


class Baralho(Iterable):
    naipes = "copas ouros espadas paus".split()
    valores = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

    def __init__(self):
        self._cartas = [
            Carta(valor, naipe)
            for naipe in self.naipes
            for valor in self.valores
        ]

    def funcao_papai(self):
        teste = 'AAAAAAAAAAAAA'
        return teste


class BaralhoInverso(Baralho):
    def funcao_papai(self):
        a = super().funcao_papai()
        return a

    def __iter__(self):
        return IteradorDoBaralho(reversed(self._cartas))


example = BaralhoInverso()
print(example.funcao_papai())

# cards = copag._cartas

# print(dir(cards))

# gapoc = BaralhoInverso()
# print(gapoc.__iter__())
# faz um exemplinho ai com next e iter.
# composicao eh quando uma classe tem uma propriedade que eh uma outra classe
