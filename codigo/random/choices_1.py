import random

frutas = ["manzana", "naranja", "frutilla"]

# 1 elección
print(random.choices(frutas))

# 10 elecciones
print(random.choices(frutas, k=10))