import re

patron = r"a?b?c?"  # a opcional, b opcional, c opcional

print(re.fullmatch(patron, ""))

print(re.fullmatch(patron, "a"))
print(re.fullmatch(patron, "b"))
print(re.fullmatch(patron, "c"))

print(re.fullmatch(patron, "ab"))
print(re.fullmatch(patron, "ac"))
print(re.fullmatch(patron, "bc"))

print(re.fullmatch(patron, "ba"))
print(re.fullmatch(patron, "ca"))
print(re.fullmatch(patron, "cb"))

print(re.fullmatch(patron, "abc"))

print(re.fullmatch(patron, "cba"))