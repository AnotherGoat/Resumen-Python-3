# Contenidos iniciales del archivo
archivo = open("archivo.txt", "r")
print(archivo.read())
archivo.close()

# Se borran los contenidos y se escribe sobre ellos
archivo = open("archivo.txt", "w")
archivo.write("¡Hola mundo!")
archivo.close()

# Contenidos nuevos
archivo = open("archivo.txt", "r")
print(archivo.read())
archivo.close()