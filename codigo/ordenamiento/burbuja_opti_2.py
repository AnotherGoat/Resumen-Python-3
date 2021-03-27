def burbuja(lista):
    N = len(lista)

    for i in range(N - 1):
        cambios = False

        for j in range(N - 1 - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                cambios = True
        
        if not cambios:
            break

    return lista

numeros = [10, -1, -5, 100, 5, -0.5, -22, 44, -100, -10, 0.5, 0, -44, 1, 22]
print(burbuja(numeros))