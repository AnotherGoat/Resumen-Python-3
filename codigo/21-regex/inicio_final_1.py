import re

# palabras que empiezan con s
patron = r"^s"

print(re.search(patron, "sandía"))
print(re.search(patron, "saludar"))
print(re.search(patron, "final"))
print(re.search(patron, "campana"))