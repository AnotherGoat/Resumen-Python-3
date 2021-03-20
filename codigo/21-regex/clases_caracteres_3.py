import re

patron = r"[abc][def]"  # a, b o c seguida de d, e o f

print(re.findall(patron, "abcdef ac ab de cd ce be fb bf be cf fa"))