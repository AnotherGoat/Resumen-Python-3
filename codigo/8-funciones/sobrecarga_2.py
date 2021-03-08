def area(x, y=None):
    if y is None:  # Cuadrado
        return x * x
    else:  # Rectángulo
        return x * y

print(area(4))  # Cuadrado
print(area(5, 6))  # Rectángulo