def burbuja(lista):
    N = len(lista)

    for i in range(N - 1):
        for j in range(N - 1):
            if lista[j] < lista[j+1]:  # condición invertida
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

numeros = [10, -1, -5, 100, 5, -0.5, -22, 44, -100, -10, 0.5, 0, -44, 1, 22]
print(burbuja(numeros))