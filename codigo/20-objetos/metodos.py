class Perro:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def ladrar(self):
        print("¡Guau!")

# instanciando la clase
fido = Perro("Fido", "blanco")

# mostrando atributos
print(fido.nombre)
print(fido.color)
# llamando métodos
fido.ladrar()