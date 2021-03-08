archivo = open("archivo.txt", "r")

print(archivo.read())
archivo.seek(0)  # Regresa a la posición 0
print(archivo.read())

archivo.close()