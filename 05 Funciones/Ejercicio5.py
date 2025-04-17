# Ejercicio 5

def segundos_a_horas(segundos):
    
    if isinstance(segundos, str):
        return print("Error: El número de segundos no puede ser un string")
    if segundos < 0:
        return print("Error: El número de segundos no puede ser negativo")
    
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos_restantes} segundos")

# segundos_a_horas(7853)