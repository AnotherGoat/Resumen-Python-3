import random

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# muestra de 5 elementos
print(random.sample(alfabeto, 5))

# muestra de 10 elementos
print(random.sample(alfabeto, 10))

# muestra de 1 elemento
print(random.sample(alfabeto, 1))