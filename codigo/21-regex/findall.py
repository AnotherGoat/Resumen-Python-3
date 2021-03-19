import re

patron = r"hola"

print(re.findall(patron, "hola mundo, chao"))
print(re.findall(patron, "holachaoholachaohola"))