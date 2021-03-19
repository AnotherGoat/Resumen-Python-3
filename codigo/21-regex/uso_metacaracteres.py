import re

# Para evitar tener que escribir esto
patron1 = "\\$"

# Se usan cadenas puras
patron2 = r"\$"

print(re.match(patron1, "$"))
print(re.match(patron2, "$"))

# Para expresiones muy largas resulta especialmente útil
patron3 = r"\$\.\?\*\+"

# En vez de
patron4 = "\\$\\.\\?\\*\\+"

print(re.match(patron3, "$.?*+"))
print(re.match(patron4, "$.?*+"))