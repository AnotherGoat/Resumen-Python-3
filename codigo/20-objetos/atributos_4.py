class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

juan = Persona("Juan", 25)
maria = Persona ("María", 27)

print(juan.nombre)
print(maria.edad)