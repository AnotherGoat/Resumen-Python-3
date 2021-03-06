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

print(firulais.nombre)  # Firulais
print(firulais.color)  # café
firulais.ladrar()  # ¡Guau!

misifu = Gato("Misifu", "blanco")

print(misifu.nombre)  # Misifu
print(misifu.color)  # Blanco
misifu.maullar()  # ¡Miau!