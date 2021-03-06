class Humano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        print("Hola, soy {}".format(self.nombre))
        print("Tengo {} años".format(self.edad))

class Trabajador(Humano):
    def __init__(self, nombre, edad, trabajo):
        super().__init__(nombre, edad)
        self.trabajo = trabajo

    def presentar(self):
        super().presentar()
        print("Soy {}".format(self.trabajo))

t = Trabajador("John", 30, "profesor")
t.presentar()
# Hola, soy John
# Tengo 30 años
# Soy profesor