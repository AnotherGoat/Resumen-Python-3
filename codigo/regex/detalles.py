import re

patron = r"pam"
resultado = re.search(patron, "foobarspameggs")

if resultado:
    print(resultado.group())
    print(resultado.start())
    print(resultado.end())
    print(resultado.span())