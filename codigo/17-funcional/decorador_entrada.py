def entrada(func):
    def envolver():
        x = int(input(': '))
        y = int(input(': '))
    func(x, y)
    return envolver

@entrada
def sumar(x, y):
    print(x + y)

@entrada
def restar(x, y):
    print(x - y)

@entrada
def multiplicar(x, y):
    print(x * y)

# Ya no necesitan argumentos para llamarse
sumar()
restar()
multiplicar()