import re

patron = r"[^A-Za-z0-9]"

# Sólo símbolos o letras con acentos extraños
print(re.findall(patron, "abcDEF789"))
print(re.findall(patron, "#.!°?)^[,-_%&$|*+"))
print(re.findall(patron, "áéíóú"))