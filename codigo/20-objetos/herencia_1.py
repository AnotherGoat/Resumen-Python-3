class Animal:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

class Gato(Animal):
    def maullar(self):
        print("¡Miau!")

class Perro(Animal):
    def ladrar(self):
        print("¡Guau!")

firulais = Perro("Firulais", "café")

print(firulais.nombre)
print(firulais.color)
firulais.ladrar()

print()  # salto de línea, para separar

misifu = Gato("Misifu", "blanco")

print(misifu.nombre)
print(misifu.color)
misifu.maullar()