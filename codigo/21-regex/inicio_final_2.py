import re

# palabras que terminan con a
patron = r"a$"

print(re.search(patron, "sandía"))
print(re.search(patron, "saludar"))
print(re.search(patron, "final"))
print(re.search(patron, "campana"))