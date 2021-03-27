a = 42  # Creación del objeto <42>
b = a  # Aumenta el contador de referencias de <42>
c = [a]  # Aumenta el contador de referencias de <42>

del a  # Reduce el contador de referencias de <42>
b = 100  # Reduce el contador de referencias de <42>
c[0] = -1  # Reduce el contador de referencias de <42>

# <42> ya puede ser eliminado