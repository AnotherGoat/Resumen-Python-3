from itertools import cycle

for i in cycle([11, "hola", 33.5, False]):
    print(i)
# 11
# hola
# 33.5
# False
# 11
# hola
# 33.5
# False
# ...