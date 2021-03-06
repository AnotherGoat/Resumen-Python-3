class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

rect = Rectangulo(5, 6)
print(Rectangulo.color)  # AttributeError
Rectangulo.pintar("azul")  # AttributeError