def ordenar(lista):
    N = len(lista)

    if N == 1:
        return lista
    
    lista1 = lista[0:N // 2]
    lista2 = lista[N // 2:N]

    lista1 = ordenar(lista1)
    lista2 = ordenar(lista2)

    return unir(lista1, lista2)

def unir(a, b):
    c = []

    while len(a) != 0 and len(b) != 0:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        
        else:
            c.append(a[0])
            a.pop(0)

    # En este punto, alguna de las 2 listas está vacía
    # Se evita hacer operaciones con listas para mostrar mejor el algoritmo

    while len(a) != 0:
        c.append(a[0])
        a.pop(0)
    
    while len(b) != 0:
        c.append(b[0])
        b.pop(0)

    return c

numeros = [10, -1, -5, 100, 5, -0.5, -22, 44, -100, -10, 0.5, 0, -44, 1, 22]
print(ordenar(numeros))