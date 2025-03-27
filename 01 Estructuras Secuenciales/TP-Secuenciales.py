# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre1 = input("Escribe tu nombre: ")
print(f"Hola {nombre1}!")

# Ejercicio 3
nombre2 = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
edad = input("Escribe tu edad: ")
residencia = input("Escribe tu lugar de residencia: ")
print(f"Soy {nombre2} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
radio = int(input("Escribe el radio de un circulo: "))
area = 3.14 * radio ** 2
perimetro = 3.14 * 2 * radio
print(f"El área del círculo es {area} y su perímetro es {perimetro}")

# Ejercicio 5
segundos = int(input("Ingresa una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

# Ejercicio 6
numero = int(input("Ingresa un numero: "))
print(f"{numero} * 1 = {numero * 1}")
print(f"{numero} * 2 = {numero * 2}")
print(f"{numero} * 3 = {numero * 3}")
print(f"{numero} * 4 = {numero * 4}")
print(f"{numero} * 5 = {numero * 5}")
print(f"{numero} * 6 = {numero * 6}")
print(f"{numero} * 7 = {numero * 7}")
print(f"{numero} * 8 = {numero * 8}")
print(f"{numero} * 9 = {numero * 9}")
print(f"{numero} * 10 = {numero * 10}")

# Ejercicio 7
numero1 = int(input("Ingresa un número entero distinto a 0: "))
numero2 = int(input("Ingresa otro número entero distinto a 0: "))
print(f"{numero1} + {numero2} = {numero1 + numero2}")
print(f"{numero1} / {numero2} = {numero1 / numero2}")
print(f"{numero1} * {numero2} = {numero1 * numero2}")
print(f"{numero1} - {numero2} = {numero1 - numero2}")

# Ejercicio 8
altura = float(input("Ingresa tu altura: "))
peso = float(input("Ingresa tu peso: "))
masaCorporal = peso / altura ** 2
print(f"Tu índice de masa corporal es {masaCorporal}")

# Ejercicio 9
celsius = float(input("Ingresa una temperatura en grado Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius} grados Celsius a Fahrenheit son {fahrenheit}")

# Ejercicio 10
primerNumero = int(input("Ingresa el primer número: "))
segundoNumero = int(input("Ingresa el segundo número: "))
tercerNumero = int(input("Ingresa el tercer número: "))
promedio = (primerNumero + segundoNumero + tercerNumero) / 3
print(f"El promedio entre {primerNumero}, {segundoNumero} y {tercerNumero} es {promedio}")