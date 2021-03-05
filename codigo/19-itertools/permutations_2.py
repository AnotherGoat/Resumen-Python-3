from itertools import permutations

letras = ("A", "B", "C")

print(list(permutations(letras)))
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]