class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

class Gato:
    def __init__(self,nombre):
        self.nombre = nombre

    def __radd__(self, otro):
        # Perro + Gato = string
        return "\t".join([self.nombre, otro.nombre])

perro = Perro("Joe")
gato = Gato("Ollie")

print(perro + gato)
# Ollie	  Joe