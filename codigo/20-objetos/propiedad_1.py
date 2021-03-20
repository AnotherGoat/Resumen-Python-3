class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @property
    def pinia_permitida(self):
        return False

pizza = Pizza(["queso", "tomate"])

print(pizza.pinia_permitida)

# No puede cambiarse el atributo
pizza.pinia_permitida = True