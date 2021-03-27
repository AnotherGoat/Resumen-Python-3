def seleccion(lista):
    N = len(lista)

    for i in range(N - 1):
        i_minimo = i

        for j in range(i + 1, N):
            if lista[j] < lista[i_minimo]:
                i_minimo = j
        
        if i_minimo != i:
            lista[i], lista[i_minimo] = lista[i_minimo], lista[i]
            print(lista)

    return lista

numeros = [2, 8, 5, 3, 9, 4, 1]
seleccion(numeros)