try:
    archivo = open("archivo.txt")
    print(archivo.read())
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    try:
        archivo.close()
    except:
        print("No se puede borrar un archivo que no existe")