import re

print(re.fullmatch(r"9{0,}" , ""))
print(re.fullmatch(r"9{0,}" , "9"))
print(re.fullmatch(r"9{0,}" , "9999999999"))

print(re.fullmatch(r"9*" , ""))
print(re.fullmatch(r"9*" , "9"))
print(re.fullmatch(r"9*" , "9999999999"))