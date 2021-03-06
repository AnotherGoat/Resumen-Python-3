class Perro:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def ladrar(self):
        print("¡Guau!")

fido = Perro("Fido", "blanco")

print(fido.nombre)  # Fido
print(fido.color)  # blanco
fido.ladrar()  # ¡Guau!