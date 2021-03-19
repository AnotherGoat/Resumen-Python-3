import re

patron = r"10"
reemplazo = "*"

print(re.sub(patron, reemplazo, "1001010101010010101101"))
print(re.sub(patron, reemplazo, "01010100011100"))