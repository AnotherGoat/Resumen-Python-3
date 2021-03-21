import re

patron = r"[A-Z0-9]*"  # cualquier cantidad de números y letras mayúsculas

print(re.fullmatch(patron, "ABC123"))
print(re.fullmatch(patron, "abc123"))
print(re.fullmatch(patron, ""))

print(re.fullmatch(patron, "A"))
print(re.fullmatch(patron, "abcd"))
print(re.fullmatch(patron, "123456"))