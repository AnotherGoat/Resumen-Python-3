def repetir_2_veces(funcion, arg):
    return funcion(funcion(arg))

def sumar5(x):
    return x + 5

print(repetir_2_veces(sumar5, 10))