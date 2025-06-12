# Ejercicio 9

def agendaActividades():
    agenda = {
        ("lunes", "10:00"): "Reunión con el equipo de desarrollo",
        ("martes", "14:00"): "Llamada con el cliente",
        ("miércoles", "09:30"): "Presentación del proyecto",
        ("jueves", "11:00"): "Revisión de código",
        ("viernes", "16:00"): "Entrega del informe semanal"
    }

    dia = input("Ingrese un día de la semana: ").lower()
    hora = input("Ingrese una hora (HH:MM): ")
    clave = (dia, hora)
    if clave in agenda:
        print(f"Actividad programada para {clave[0]} a las {clave[1]}: {agenda[clave]}")
    else:
        print(f"No hay actividades programadas para {clave[0]} a las {clave[1]}.")

agendaActividades()