import re

patron = r"hola"

# Coincidencias parciales
print(re.match(patron, "hola"))
print(re.match(patron, "hola mundo"))

# Coincidencias exactas
print(re.fullmatch(patron, "hola"))
print(re.fullmatch(patron, "hola mundo"))