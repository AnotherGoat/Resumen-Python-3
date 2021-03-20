import re

# palabras que empiezan con s y terminan con a
patron = r"^sa$"

print(re.search(patron, "sandía"))
print(re.search(patron, "saludar"))
print(re.search(patron, "final"))
print(re.search(patron, "campana"))