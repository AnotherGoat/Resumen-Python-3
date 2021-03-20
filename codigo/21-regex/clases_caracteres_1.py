import re

patron = r"[aeiou]"  # cualquier cadena con vocales minúsculas

print(re.search(patron, "Python"))
print(re.search(patron, "C"))
print(re.search(patron, "Java"))
print(re.search(patron, "C++"))