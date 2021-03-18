import random

dado_trucado = [1, 2, 3, 4, 5, 6]

# dado trucado para que sea más probable obtener un 3
#                           dado_trucado = [1, 2, 3, 4, 5, 6],   10 tiradas
print(random.choices(dado_trucado, weights=[1, 1, 6, 1, 1, 1], k=10))