import re

print(re.findall(r"[j-s]", "abcdefghijklmnopqrstuvwxyz"))

# Lo contrario al anterior
print(re.findall(r"[a-it-z]", "abcdefghijklmnopqrstuvwxyz"))

print(re.findall(r"[1-5]", "1234567890"))

print(re.findall(r"[1-5][0-9]", "4, 5, 10, 19, 25, 44, 49, 59, 60, 75, 92"))