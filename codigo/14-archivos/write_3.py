archivo = open("archivo.txt", "w")

bytes_escritos = archivo.write("¡Hola mundo!")
print(bytes_escritos)

archivo.close()