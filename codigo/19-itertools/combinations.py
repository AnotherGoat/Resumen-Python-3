from itertools import combinations

letras  = ("A", "B", "C")

print(list(combinations(letras, 1)))
# [('A',), ('B',), ('C',)]
print(list(combinations(letras, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(combinations(letras, 3)))
# [('A', 'B', 'C')]
print(list(combinations(letras, 4)))
# [] (porque es imposible, ya que sólo tiene 3 elementos)