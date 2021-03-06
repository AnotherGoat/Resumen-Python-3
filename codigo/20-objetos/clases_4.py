class Perro:
    # atributo de clase
    patas = 4

    # constructor
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

fido = Perro("Fido", "blanco")

print(fido.patas)  # 4
print(Perro.patas)  # 4