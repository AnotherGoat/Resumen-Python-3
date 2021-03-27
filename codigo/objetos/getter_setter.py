class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self.pinia_permitida = False
    
    @property
    def pinia_permitida(self):
        return self.pinia_permitida
    
    @pinia_permitida.setter
    def pinia_permitida(self, valor):
        if valor:
            contrasena = input("Ingrese la contraseña: ")
            if contrasena == "1234":
                self.pinia_permitida = valor
        else:
            raise ValueError("Alerta, ¡un intruso!")

pizza = Pizza(["queso", "tomate"])
print(pizza.pinia_permitida)

pizza.pinia_permitida = True
print(pizza.pinia_permitida)