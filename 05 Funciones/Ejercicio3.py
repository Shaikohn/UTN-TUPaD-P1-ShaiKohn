# Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    if isinstance(nombre, str) and isinstance(apellido, str) and isinstance(residencia, str):
        if isinstance(edad, int) and edad > 0:
            return print(f"Hola {nombre} {apellido}, tienes {edad} años y vives en {residencia}.")
        else:
            return print("Error: La edad debe ser un número entero positivo.")
    else:
        return print("Error: El nombre, apellido y residencia deben ser strings.")
    
# informacion_personal("Shai", "Kohn", 21, "Argentina")