import re

# cualquier cantidad de "spam" seguida de cualquier cantidad de "eggs"
patron = r"(spam)*(eggs)*"

print(re.fullmatch(patron, ""))
print(re.fullmatch(patron, "spam"))
print(re.fullmatch(patron, "eggs"))
print()

print(re.fullmatch(patron, "spameggs"))
print(re.fullmatch(patron, "spamspameggseggs"))
print(re.fullmatch(patron, "spamspamspamspameggs"))
print(re.fullmatch(patron, "spameggseggseggseggs"))
print()

print(re.fullmatch(patron, "spamegg"))
print(re.fullmatch(patron, "spameggsspam"))