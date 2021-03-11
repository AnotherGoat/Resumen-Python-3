def repetir2veces(funcion, arg):
    return funcion(funcion(arg))

def sumar5(x):
    return x + 5

print(repetir2veces(sumar5, 10))