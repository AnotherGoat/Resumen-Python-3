import re

patron = r"hola.mundo"

print(re.fullmatch(patron, "hola\nmundo"))