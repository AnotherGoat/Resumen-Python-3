import re

# palabras que empiezan con s
patron = r"^s"

print(re.match(patron, "sandía"))
print(re.match(patron, "saludar"))
print(re.match(patron, "final"))
print(re.match(patron, "campana"))

# a fullmatch() le falta información para poder aceptar todos los casos
print(re.fullmatch(patron, "sandía"))
print(re.fullmatch(patron, "saludar"))
print(re.fullmatch(patron, "final"))
print(re.fullmatch(patron, "campana"))