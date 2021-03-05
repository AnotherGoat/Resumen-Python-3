from itertools import permutations

letras  = ("A", "B")

print(list(permutations(letras, 1)))
# [('A',), ('B',)]
print(list(permutations(letras, 2)))
# [('A', 'B'), ('B', 'A')]
print(list(permutations(letras, 3)))
# [] (porque es imposible, ya que sólo tiene 2 elementos)