# Ejercicio 1

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def factorial_recursivo_hasta_1(n):
    if n == 0:
        return 1
    else:
        print(f"El factorial de {n} es {factorial_recursivo(n)} ")
        return factorial_recursivo_hasta_1(n - 1)
    
# factorial_recursivo_hasta_1(5)
