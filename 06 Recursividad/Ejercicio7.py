# Ejercicio 7

def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

# print("La cantidad de bloques es:", contar_bloques(4))