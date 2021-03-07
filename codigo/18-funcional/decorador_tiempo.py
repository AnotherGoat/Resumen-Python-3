import time

def tiempo_transcurrido(f):
    def envolver(*n):  # *n significa cualquier número de argumentos
        t1 = time.time()
        f(*n)
        t2 = time.time()
        tiempo = (t2 - t1) * 1000
        print("Tiempo transcurrido: {} ms".format(tiempo))
    return envolver

@tiempo_transcurrido
def suma_grande():
    numeros = [i for i in range(0, 1000000)]
    print("Suma: {}".format(sum(numeros)))

suma_grande()