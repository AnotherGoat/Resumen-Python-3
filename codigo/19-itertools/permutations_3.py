from itertools import permutations

letras  = ("A", "B")

print(list(permutations(letras, 1)))
print(list(permutations(letras, 2)))
print(list(permutations(letras, 3)))
# [] (porque es imposible, ya que sólo tiene 2 elementos)