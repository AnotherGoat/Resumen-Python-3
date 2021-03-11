def decor(func):
    def envolver():
        print("=" * 12)
        func()
        print("=" * 12)
    return envolver

@decor  # nombre del decorador
def imprimir_texto():
    print("¡Hola mundo!")