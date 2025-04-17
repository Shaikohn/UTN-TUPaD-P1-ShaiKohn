# Ejercicio 4

# Tambien podría haber modularizado con una funcion que haga directamente la validación
# del radio, pero no lo hice porque se especifica que llamemos a estas funciones
# y no a una función que las llame a ellas.

def calcular_area_circulo(radio):
    if isinstance(radio, str):
        return print("Error: El radio no puede ser un string")
    if radio < 0:
        return print("Error: El radio no puede ser negativo")
    pi = 3.14159
    area = pi * (radio ** 2)
    return print(f"El área del círculo es: {area}")

def calcular_perimetro_circulo(radio):
    if isinstance(radio, str):
        return print("Error: El radio no puede ser un string")
    if radio < 0:
        return print("Error: El radio no puede ser negativo")
    pi = 3.14159
    perimetro = 2 * pi * radio
    return print(f"El perímetro del círculo es: {perimetro}")

# calcular_area_circulo(8)
# calcular_perimetro_circulo(20)