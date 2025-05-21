# Ejercicio 2

def valor_posicion_en_fibonacci(posicion):
    if posicion <= 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return valor_posicion_en_fibonacci(posicion - 1) + valor_posicion_en_fibonacci(posicion - 2)
    
def fibonacci_hasta_1(posicion):
    if posicion == 0:
        return 0
    else:
        print(f"El valor de la posicion {posicion} en la serie de Fibonacci es {valor_posicion_en_fibonacci(posicion)}")
        return fibonacci_hasta_1(posicion - 1)

# fibonacci_hasta_1(5)