class Gato:
    # Constructor
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad

felix = Gato("café", 7)  # Instancia (objeto) de la clase Gato

print(felix.color)  # café
print(felix.edad)  # 7