archivo = open("archivo.txt", "r")

print(archivo.read(16))
print(archivo.tell())

archivo.close()