def es_par(n):
    if n == 0:
        return True
    else:
        return es_impar(n-1)

def es_impar(n):
    return not es_par(n)

print(es_impar(17))
print(es_par(23))