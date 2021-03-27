import re

palabra = "3733234233432348393333133"

print(re.sub(r"3", "", palabra))
print(re.sub(r"3", "", palabra, count=0))