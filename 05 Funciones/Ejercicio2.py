# Ejercicio 2

def saludar_usuario(nombre):
    if isinstance(nombre, str):
        return print(f"Hola {nombre}!")
    else:
        return print("Error: El nombre no puede ser un número")
    
# saludar_usuario("Shai")