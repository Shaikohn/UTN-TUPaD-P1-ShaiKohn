# Ejercicio 7

def estudiantesAprobados():
    parciales1 = {101, 102, 103, 104, 105}
    parciales2 = {103, 104, 106, 107}
    # Se usan funciones de conjuntos para realizar las operaciones
    aprobados_ambos = parciales1.intersection(parciales2)
    aprobados_solo_uno = parciales1.symmetric_difference(parciales2)
    total_aprobados = parciales1.union(parciales2)

    print(f"Estudiantes que aprobaron ambos parciales: {aprobados_ambos}")
    print(f"Estudiantes que aprobaron solo uno de los dos: {aprobados_solo_uno}")
    print(f"Lista total de estudiantes que aprobaron al menos un parcial: {total_aprobados}")

estudiantesAprobados()