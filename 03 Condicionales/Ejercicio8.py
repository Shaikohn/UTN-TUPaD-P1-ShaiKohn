# Ejercicio 8

nombre = input("Ingrese su nombre: ")
print("Ingresa 1 si quiere que su nombre esté en mayúsculas, 2 si quiere que esté en minúsculas o 3 si quiere que esté con la primera letra en mayúscula.")
elegirNumero = int(input("Ingrese 1, 2 o 3: "))
if elegirNumero == 1:
    print(nombre.upper())
elif elegirNumero == 2:
    print(nombre.lower())
elif elegirNumero == 3:
    print(nombre.title())