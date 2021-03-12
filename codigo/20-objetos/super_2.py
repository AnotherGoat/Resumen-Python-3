class Humano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print("Hola, soy {}".format(self.nombre))
        print("Tengo {} años".format(self.edad))

class Trabajador(Humano):
    def __init__(self, nombre, edad, trabajo):
        super().__init__(nombre, edad)
        self.trabajo = trabajo

    def presentarse(self):
        super().presentarse()
        print("Soy {}".format(self.trabajo))

h = Humano("Javier", 20)
h.presentarse()

print()

t = Trabajador("John", 30, "profesor")
t.presentarse()