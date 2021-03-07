primero = {1, 2, 3, 4, 5, 6}
segundo = {4, 5, 6, 7, 8, 9}

# Diferencia simétrica
print(primero ^ segundo)  # {1, 2, 3, 7, 8, 9}
# Forma equivalente
print((primero | segundo) - (primero & segundo))  # {1, 2, 3, 7, 8, 9}