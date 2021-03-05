from itertools import count

for i in count(3, 2):  # Empieza desde 3, contando de 2 en 2
    print(i)
    if i >= 20:  # Termina en 20
        break