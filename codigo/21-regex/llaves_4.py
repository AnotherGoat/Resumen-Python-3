import re

print(re.fullmatch(r"9{1,}" , ""))
print(re.fullmatch(r"9{1,}" , "9"))
print(re.fullmatch(r"9{1,}" , "9999999999"))

print(re.fullmatch(r"9+" , ""))
print(re.fullmatch(r"9+" , "9"))
print(re.fullmatch(r"9+" , "9999999999"))