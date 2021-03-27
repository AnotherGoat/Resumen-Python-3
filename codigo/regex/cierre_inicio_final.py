import re

empieza_s = r"^s.*"  # palabras que empiezan con s
termina_a = r".*a$"  # palabras que terminan con a
s_a = r"^s.*a$"  # palabras que empiezan con s y terminan con a

# ahora ya funciona fullmatch()
print(re.fullmatch(empieza_s, "sandía"))
print(re.fullmatch(empieza_s, "saludar"))
print(re.fullmatch(empieza_s, "final"))
print(re.fullmatch(empieza_s, "campana"))
print()

print(re.fullmatch(termina_a, "sandía"))
print(re.fullmatch(termina_a, "saludar"))
print(re.fullmatch(termina_a, "final"))
print(re.fullmatch(termina_a, "campana"))
print()

print(re.fullmatch(s_a, "sandía"))
print(re.fullmatch(s_a, "saludar"))
print(re.fullmatch(s_a, "final"))
print(re.fullmatch(s_a, "campana"))