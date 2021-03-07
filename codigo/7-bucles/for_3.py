numeros = [1, 9, 8, 2, 1, 0, 0, 2, 4, 0, 3, 5, 6, 8]
for n in numeros:

    if n == 0:
        continue
    if n == 3:
        break
    
    print(n)
# muestra los números de la lista, omitiendo los 0 y termina cuando llega al 3