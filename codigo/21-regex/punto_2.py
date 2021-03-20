import re

patron = r"hola.mundo"

print(re.match(patron, "hola\nmundo"))