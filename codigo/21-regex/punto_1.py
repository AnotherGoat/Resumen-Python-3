import re

patron = r"c.lor"

print(re.fullmatch(patron, "color"))
print(re.fullmatch(patron, "calor"))
print(re.fullmatch(patron, "collar"))