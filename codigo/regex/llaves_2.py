import re

print(re.fullmatch(r"9{0,1}" , ""))
print(re.fullmatch(r"9{0,1}" , "9"))
print(re.fullmatch(r"9{0,1}" , "99"))

print(re.fullmatch(r"9?" , ""))
print(re.fullmatch(r"9?" , "9"))
print(re.fullmatch(r"9?" , "99"))