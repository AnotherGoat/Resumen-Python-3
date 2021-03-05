def decor1(func):
    def envolver():
        print("=" * 12)
        func()
        print("=" * 12)
    return envolver

def decor2(func):
    def envolver():
        print("*" * 12)
        func()
        print("*" * 12)
    return envolver

@decor2
@decor1
@decor2
def imprimir_texto():
    print("¡Hola mundo!")

imprimir_texto()
# ************
# ============
# ************
# ¡Hola mundo!
# ************
# ============
# ************