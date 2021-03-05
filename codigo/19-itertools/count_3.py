from itertools import count

for i in count(100, -5):  # Empieza desde 3, contando de -5 en -5
    print(i)
    if i >= 20:  # Termina en 20
        break