# Ejercicio 1

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad.")

# Ejercicio 2

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Ejercicio 4

edadUsuario = int(input("Ingrese su edad: "))
if edadUsuario < 12:
    print("El usuario es un niño/a.")
elif edadUsuario >= 12 and edadUsuario < 18:
    print("El usuario es un adolescente.")
elif edadUsuario >= 18 and edadUsuario < 30:
    print("El usuario es un/a adulto/a joven.")
elif edadUsuario >= 30:
    print("El usuario es un/a adulto/a.")

# Ejercicio 5

contrasena = input("Ingrese su contraseña: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Ejercicio 6

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
from statistics import mode, median, mean
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
print(numeros_aleatorios)
if media > mediana and moda > media:
    print("Hay sesgo positivo.") 
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo.")
else:
    print("No hay sesgo.")

# Ejercicio 7

frase = input("Ingrese una frase o palabra: ")
if frase.endswith('a') or frase.endswith('A') or frase.endswith('e') or frase.endswith('E') or frase.endswith('i') or frase.endswith('I') or frase.endswith('o') or frase.endswith('O') or frase.endswith('u') or frase.endswith('U'):
    frase = frase + "!"
    print(frase)
else:
    print(frase)

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

# Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")

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