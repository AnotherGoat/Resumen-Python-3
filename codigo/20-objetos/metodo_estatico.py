class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @staticmethod
    def validar_topping(topping):
        if topping == "piña":
            raise ValueError("¡No se aceptan piñas!")
        else:
            return True

ingredientes = ["queso", "cebollas", "spam"]

if all(Pizza.validar_topping(i) for i in ingredientes):
    pizza = Pizza(ingredientes)