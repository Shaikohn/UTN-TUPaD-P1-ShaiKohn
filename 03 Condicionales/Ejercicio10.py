# Ejercicio 10

hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = input("Ingrese el mes (1-12): ")
dia = int(input("Ingrese el día: "))
if hemisferio == "N":
    if mes == "3" and dia >= 20 or mes == "4" or mes == "5" or mes == "6" and dia < 21:
        print("Es primavera.")
    elif mes == "6" and dia >= 21 or mes == "7" or mes == "8" or mes == "9" and dia < 23:
        print("Es verano.")
    elif mes == "9" and dia >= 23 or mes == "10" or mes == "11" or mes == "12" and dia < 21:
        print("Es otoño.")
    elif mes == "12" and dia >= 21 or mes == "1" or mes == "2" and dia < 20:
        print("Es invierno.")
if hemisferio == "S":
    if mes == "3" and dia >= 20 or mes == "4" or mes == "5" or mes == "6" and dia < 21:
        print("Es otoño.")
    elif mes == "6" and dia >= 21 or mes == "7" or mes == "8" or mes == "9" and dia < 23:
        print("Es invierno.")
    elif mes == "9" and dia >= 23 or mes == "10" or mes == "11" or mes == "12" and dia < 21:
        print("Es primavera.")
    elif mes == "12" and dia >= 21 or mes == "1" or mes == "2" and dia < 20:
        print("Es verano.")