def area(x, y=None):
    if y is None:  # Cuadrado
        return x * x
    else:  # Rectángulo
        return x * y

area(4)  # 16, cuadrado
area(5, 6)  # 30, rectángulo