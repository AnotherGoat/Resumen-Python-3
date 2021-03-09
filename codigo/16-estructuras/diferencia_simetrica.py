primero = {1, 2, 3, 4, 5, 6}
segundo = {4, 5, 6, 7, 8, 9}

# Diferencia simétrica
print(primero ^ segundo)

# Se obtiene el mismo resultado usando otras operaciones
print((primero | segundo) - (primero & segundo))