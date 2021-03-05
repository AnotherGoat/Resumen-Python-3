archivo = open("archivo.txt", "r")

print(archivo.read())
print(archivo.read())  # Cadena vacía

archivo.close()