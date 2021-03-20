class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    def calcular_area(self):
        return self.ancho * self.altura
    
    @classmethod
    def crear_cuadrado(cls, lado):
        return cls(lado, lado)

# Crea un cuadrado de lado 5
cuadrado = Rectangulo.crear_cuadrado(5)

print(cuadrado.calcular_area())