# Ejercicio 6

def notasAlumnos():
    alumnos = {}
    while len(alumnos) < 3:
        notas = ()
        nombre = input("Ingrese el nombre del alumno: ")
        while len(notas) < 3:
            nota = int(input("Ingrese la nota del alumno: "))
            notas += (nota,)
        alumnos[nombre] = notas
    print("Alumnos y sus notas:")
    for nombre, notas in alumnos.items():
        print(f"{nombre}: {notas}")

notasAlumnos()