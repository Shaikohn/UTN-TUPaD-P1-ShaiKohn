# Ejercicio 3

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

# Decide hacer un algoritmo parecido a los del ejercicio 1 y 2, para probar la funcion hecha
def potencia_recursiva_hasta_1(base, exponente):
    if exponente == 0:
        return 1
    else:
        print(f"La potencia de {base} elevado a {exponente} es {potencia_recursiva(base, exponente)}")
        return potencia_recursiva_hasta_1(base, exponente - 1)

# potencia_recursiva_hasta_1(2, 5)