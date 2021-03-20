class Persona:
    def __init__(self, edad):
        self.edad = int(edad)
    
    @property
    def es_adulto(self):
        return self.edad >= 18