archivo = open("archivo.txt", "r")

print(archivo.read())
archivo.seek(16)  # Regresa a la posición 16
print(archivo.read())

archivo.close()