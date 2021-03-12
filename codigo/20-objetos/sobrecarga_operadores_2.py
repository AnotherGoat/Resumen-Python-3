# Si x e y son del mismo tipo y este tipo tiene implementado los métodos mágicos
x = 10
y = 5

resultado = [
    x + y == x.__add__(y),
    x - y == x.__sub__(y),
    x * y == x.__mul__(y),
    x / y == x.__truediv__(y),
    x // y == x.__floordiv__(y),
    x % y == x.__mod__(y),
    x ** y == x.__pow__(y),
    x & y == x.__and__(y),
    x ^ y == x.__xor__(y),
    x | y == x.__or__(y)
]

print(resultado)