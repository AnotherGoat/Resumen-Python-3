import os

directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_relativa = "archivo.txt"
ruta_absoluta = os.path.join(directorio_script, ruta_relativa)

archivo = open(ruta_absoluta)

# para ver las rutas y entender qué ocurrió
print(directorio_script)
print(ruta_relativa)
print(ruta_absoluta)