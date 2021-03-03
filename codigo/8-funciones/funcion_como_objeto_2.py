def sumar(x, y):
    return x + y

def repetir2veces(funcion, x, y):
    return funcion(funcion(x, y), funcion(x, y))

a = 5
b = 10

print(repetir2veces(sumar, a, b))
# sumar(sumar(5, 10), sumar(5, 10))
# sumar(5 + 10, 5 + 10)
# sumar(15, 15)
# 15 + 15
# 30