import re

patron = r"hola"

print(re.search(patron, "hola"))
print(re.search(patron, "hola mundo"))
print(re.search(patron, "ola"))
print(re.search(patron, "chao hola"))