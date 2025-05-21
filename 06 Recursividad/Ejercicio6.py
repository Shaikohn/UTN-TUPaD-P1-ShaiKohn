# Ejercicio 6

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

# print(suma_digitos(1234))