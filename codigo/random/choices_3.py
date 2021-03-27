import random

frutas = ["manzana", "naranja", "frutilla"]

# los siguientes ejemplos son equivalentes
random.seed(1000)
print(random.choices(frutas, weights=[2, 6, 3], k=5))

random.seed(1000)
print(random.choices(frutas, cum_weights=[2, 8, 11], k=5))
#                                      [2, 2+6, 2+6+3]