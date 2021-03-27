archivo = open("archivo.txt", "r")

print(archivo.read(16))
print(archivo.read(8))
print(archivo.read(4))
print(archivo.read())

archivo.close()