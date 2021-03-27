import re

patron = r"....."  # cadenas de 5 caracteres

print(re.fullmatch(patron, "verde"))
print(re.fullmatch(patron, "12345"))
print(re.fullmatch(patron, "@!/&?"))

print(re.fullmatch(patron, ""))

# si se usa match(), serían de 5 o más caracteres
print(re.fullmatch(patron, "qwertyuiopasdfghjklzxcvbnm"))
print(re.match(patron, "qwertyuiopasdfghjklzxcvbnm"))