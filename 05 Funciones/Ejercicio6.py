# Ejercicio 6

def tabla_multiplicar(numero):
    if isinstance(numero, str):
        return print("Error: El número no puede ser un string")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# tabla_multiplicar(13)