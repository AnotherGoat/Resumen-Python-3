def decor(func):
    def envolver():
        print("=" * 12)
        func()
        print("=" * 12)
    return envolver

def imprimir_texto():
    print("¡Hola mundo!")

texto_decorado = decor(imprimir_texto)
texto_decorado()