def insercion(lista):
    N = len(lista)

    for i in range(1, N):
        j = i

        while j > 0 and lista[j-1] < lista[j]:  # condición invertida
            lista[j-1], lista[j] = lista[j], lista[j-1]

            j -= 1

    return lista

numeros = [10, -1, -5, 100, 5, -0.5, -22, 44, -100, -10, 0.5, 0, -44, 1, 22]
print(insercion(numeros))