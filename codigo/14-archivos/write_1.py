# Escribe sobre el archivo
archivo = open("archivo.txt", "w")
archivo.write("¡Hola mundo!")
archivo.close()

# Muestra el texto del archivo
archivo = open("archivo.txt", "r")
print(archivo.read())
archivo.close()