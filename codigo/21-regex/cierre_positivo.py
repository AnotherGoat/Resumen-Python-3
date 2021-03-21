import re

patron = r"g+"  # 1 o más letras g

print(re.fullmatch(patron, ""))
print(re.fullmatch(patron, "g"))
print(re.fullmatch(patron, "gg"))
print(re.fullmatch(patron, "gggggggggggggggggg"))