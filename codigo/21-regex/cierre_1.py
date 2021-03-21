import re

patron = r"V*"  # 0 más letras V

print(re.fullmatch(patron, "V"))
print(re.fullmatch(patron, "VV"))
print(re.fullmatch(patron, "VVVVVV"))
print(re.fullmatch(patron, ""))
print(re.fullmatch(patron, "B"))

print(re.fullmatch(patron, "VVVVBBBB"))
print(re.fullmatch(r"V*B*", "VVVVBBBB"))