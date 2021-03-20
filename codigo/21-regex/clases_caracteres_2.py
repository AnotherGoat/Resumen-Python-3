import re

patron = r"[aeiou]"  # cualquier cadena con vocales minúsculas

print(re.findall(patron, "Python es un lenguaje de programación"))