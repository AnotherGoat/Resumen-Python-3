import random

frutas = ["manzana", "naranja", "frutilla"]

# los siguientes ejemplos son equivalentes
random.seed(100)
print(random.choices(frutas, weights=[2, 6, 3], k=5))

random.seed(100)
print(random.choices(frutas, weights=[20, 60, 30], k=5))

random.seed(100)
print(random.choices(frutas, weights=[0.2, 0.6, 0.3], k=5))

random.seed(100)
print(random.choices(frutas, weights=[2000000, 6000000, 3000000], k=5))