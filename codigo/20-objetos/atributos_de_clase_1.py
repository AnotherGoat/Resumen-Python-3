class Perro:
    # atributo de clase
    patas = 4

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

fido = Perro("Fido", "blanco")

# accedido desde un objeto
print(fido.patas)
# accedido desde la clase
print(Perro.patas)