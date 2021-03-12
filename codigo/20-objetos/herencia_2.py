class Lobo:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def ladrar(self):
        print("Grrr...")

class Perro(Lobo):
    # hereda el constructor de lobo

    # sobreescribe el método ladrar() de Lobo
    def ladrar(self):
        print("Guau")

husky = Perro("Max", "gris")
husky.ladrar()