import re

patron = r"9{1,3}"  # entre 1 y 3 números 9

print(re.fullmatch(patron , ""))
print(re.fullmatch(patron , "9"))
print(re.fullmatch(patron , "99"))
print(re.fullmatch(patron , "999"))
print(re.fullmatch(patron , "9999"))