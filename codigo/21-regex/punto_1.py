import re

patron = r"c.lor"

print(re.match(patron, "color"))
print(re.match(patron, "calor"))
print(re.match(patron, "collar"))