from itertools import product

letras1 = ("A", "B")
letras2 = ("C", "D")

print(list(product(letras1, letras2)))
# [('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]