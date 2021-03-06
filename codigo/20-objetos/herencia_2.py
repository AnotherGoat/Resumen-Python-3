class Lobo:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def ladrar(self):
        print("Grrr...")

class Perro(Lobo):
    def ladrar(self):
        print("Guau")

husky = Perro("Max", "gris")
husky.bark()  # Guau