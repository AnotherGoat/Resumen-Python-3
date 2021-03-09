def seleccion(lista):
    N = len(lista)

    for i in range(N - 1):
        i_minimo = i

        for j in range(i + 1, N):
            if lista[j] < lista[i_minimo]:
                i_minimo = j
        
        if i_minimo != i:
            lista[i], lista[i_minimo] = lista[i_minimo], lista[i]

    return lista

numeros = [10, -1, -5, 100, 5, -0.5, -22, 44, -100, -10, 0.5, 0, -44, 1, 22]
print(seleccion(numeros))