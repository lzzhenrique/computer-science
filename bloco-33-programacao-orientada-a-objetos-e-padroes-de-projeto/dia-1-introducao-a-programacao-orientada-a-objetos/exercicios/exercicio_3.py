# Abstracao
# Circulo

# atributos
# raio
# PI

# comportamento
# calcular area
# calcular perimetro

# verificacoes dentro da classe nao rola. Ou nao rola so com return e if

class Circle:
    def __init__(self, radius, diameter):
        self.radius = radius
        self.PI = 3.14
        self.diameter = diameter
        self.length = 2 * (radius * self.PI)

    def calculate_area(self):
        result = self.PI * (self.radius * self.radius)
        return result

    def calculate_perimeter(self):
        result = self.length / self.diameter
        return result


circle = Circle(radius=5, diameter=10)
print(circle)
print(circle.calculate_area())
print(circle.calculate_perimeter())
