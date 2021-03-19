import re

patron = r"10"

print(len(re.findall(patron, "1001010101010010101101")))
print(len(re.findall(patron, "01010100011100")))