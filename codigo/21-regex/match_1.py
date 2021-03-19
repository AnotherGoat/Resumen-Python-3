import re

patron = r"hola"

print(re.match(patron, "hola"))
print(re.match(patron, "hola mundo"))
print(re.match(patron, "ola"))
print(re.match(patron, "chao hola"))