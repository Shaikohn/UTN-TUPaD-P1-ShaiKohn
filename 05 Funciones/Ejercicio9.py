# Ejercicio 9

def celcius_a_fahrenheit(celsius):
    if isinstance(celsius, str):
        return print("Error: La temperatura no puede ser un string")
    fahrenheit = (celsius * 9/5) + 32
    return print(f"{celsius}°C son {fahrenheit}°F")

# celcius_a_fahrenheit(12)