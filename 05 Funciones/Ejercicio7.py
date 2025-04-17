# Ejercicio 7

def operaciones_basicas(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return print("Error: Los números no pueden ser strings")
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = round(a / b, 2) if b != 0 else "Error: División por cero"
    
    print(f"{a} + {b} = {suma}")
    print(f"{a} - {b} = {resta}")
    print(f"{a} * {b} = {multiplicacion}")
    print(f"{a} / {b} = {division}")

# operaciones_basicas(100, 65)