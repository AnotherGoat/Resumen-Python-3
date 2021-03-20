import re

print(re.findall(r"[A-Za-z]", "PascalCase"))
print(re.findall(r"[0-9A-Z]", "HOLA123"))