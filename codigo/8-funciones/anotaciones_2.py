def sumar(x: int, y: int) -> int:
    return x + y

# Uso esperado:
print(sumar(10, 5))  # 15

# Usos válidos pero no esperados:
print(sumar(10.2, 7.4))  # 17.6
print(sumar('a', 'b'))  # ab