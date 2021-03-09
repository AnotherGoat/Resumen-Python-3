def insercion(lista):
    N = len(lista)

    for i in range(1, N):
        j = i

        while j > 0 and lista[j-1] > lista[j]:
            lista[j-1], lista[j] = lista[j], lista[j-1]
            print(lista)

            j -= 1

    return lista

numeros = [2, 8, 5, 3, 9, 4, 1]
insercion(numeros)