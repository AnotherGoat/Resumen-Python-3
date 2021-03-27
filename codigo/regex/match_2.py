import re

patron = r"hola"

print(bool(re.match(patron, "hola")))
print(bool(re.match(patron, "hola mundo")))
print(bool(re.match(patron, "ola")))
print(bool(re.match(patron, "chao hola")))