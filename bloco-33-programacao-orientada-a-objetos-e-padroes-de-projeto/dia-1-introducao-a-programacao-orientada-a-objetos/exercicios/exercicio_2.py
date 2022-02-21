# Abstracao
# Retangulo

# atributos
# altura
# base

# comportamento
# calcular area
# calcular perimetro

class Rectangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def calculate_area(self):
        result = self.height * self.base
        return result

    def calculate_perimeter(self):
        result = 2 * (self.base + self.height)
        return result


retangle = Rectangle(height=9, base=1)

print(retangle.calculate_area())
print(retangle.calculate_perimeter())
