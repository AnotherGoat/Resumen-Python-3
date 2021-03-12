class Perro:
    patas = 4

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

fido = Perro("Fido", "blanco")

# valores por defecto
print(fido.patas)
print(Perro.patas)

Perro.patas = 5
# cambian el valor para la clase y todos los objetos
print(fido.patas)
print(Perro.patas)

fido.patas = 6
# sólo cambia el valor para un objeto
print(fido.patas)
print(Perro.patas)