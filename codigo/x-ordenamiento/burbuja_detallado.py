def burbuja(lista):
    N = len(lista)

    for i in range(N - 1):
        for j in range(N - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)

    return lista

numeros = [2, 8, 5, 3, 9, 4, 1]
burbuja(numeros)