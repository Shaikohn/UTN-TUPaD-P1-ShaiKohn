# Ejercicio 10

def calcular_promedio(a, b, c):
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return print("Error: Los números no pueden ser strings")
    if a < 0 or b < 0 or c < 0:
        return print("Error: Los números deben ser mayores que cero")
    promedio = round((a + b + c) / 3, 2)
    return print(f"El promedio de {a}, {b} y {c} es: {promedio}")

# calcular_promedio(3, 7, 1)