import re

patron = r"Juan"
reemplazo = "Javier"
cadena = "Hola, soy Juan"

print(re.sub(patron, reemplazo, cadena))