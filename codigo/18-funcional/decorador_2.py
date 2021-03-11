def decor(func):
    def envolver():
        print("=" * 12)
        func()
        print("=" * 12)
    return envolver

def imprimir_texto():
    print("¡Hola mundo!")

imprimir_texto()
print()

imprimir_texto = decor(imprimir_texto)
imprimir_texto()
print()

imprimir_texto = decor(imprimir_texto)
imprimir_texto()