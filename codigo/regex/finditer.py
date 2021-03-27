import re

patron = r"hola"

print(re.finditer(patron, "hola mundo, chao"))
print(re.finditer(patron, "holachaoholachaohola"))