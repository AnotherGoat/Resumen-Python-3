import re

patron = r"....."  # cadenas de 5 o más caracteres

print(re.match(patron, "verde"))
print(re.match(patron, "12345"))
print(re.match(patron, "@!/&?"))

print(re.match(patron, ""))

print(re.match(patron, "qwertyuiopasdfghjklzxcvbnm"))