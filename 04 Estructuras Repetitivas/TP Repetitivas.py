# Ejercicio 1

for i in range(0, 101):
    print(i)

# Ejercicio 2

cont = 0
num = int(input("Ingrese un número entero positivo: "))

while num >= 1:
    cont += 1
    num //= 10

print("La cantidad de dígitos es:", cont)

# Ejercicio 3

num1 = int(input("Ingrese un número entero positivo: "))
num2 = int(input("Ingrese otro número entero positivo: "))
menor = 0
mayor = 0
suma = 0
if(num1 >= num2):
    menor = num2
    mayor = num1
else:
    menor = num1
    mayor = num2

for i in range(menor + 1, mayor, + 1):
    suma += i
    
print("La suma de los números entre", menor, "y", mayor, " excluyendo esos valores es:", suma)

# Ejercicio 4

num = int(input("Ingrese un número entero positivo: "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingrese un número entero positivo: "))

print("El total acumulado es:", suma)

# Ejercicio 5

from random import randint

num = randint(0, 9)
numUsuario = int(input("Ingrese un número entre 0 y 9: "))
intentos = 0

while num != numUsuario:
    numUsuario = int(input("Ingrese otro número entre 0 y 9: "))
    intentos += 1

print("El número era:", num)
print("Adivinaste el número en", intentos, "intentos")

# Ejercicio 6

for i in range(100, 1, -1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7

num = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(0, num + 1):
    suma += i

print("La suma de los números comprendidos entre 0 y", num, "es:", suma)

# Ejercicio 8

pares = 0
impares = 0
negativos = 0
positivos = 0
# Basta con cambiar el 10 por 100 para que el programa funcione con 100 números
cantNum = 10
for i in range(cantNum):
    num = int(input("Ingrese un número entero: "))

    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("////////////////////")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números positivos:", positivos)

# Ejercicio 9

suma = 0
media = 0
# Basta con cambiar el 10 por 100 para que el programa funcione con 100 números
cantNum = 10
for i in range(cantNum):
    num = int(input("Ingrese un número entero positivo: "))

    suma += num

media = suma / cantNum
print("////////////////////")
print("La media de los números es:", media)

# Ejercicio 10

num = int(input("Ingrese un número entero positivo: "))
numInvertido = ""

while num > 0:
    digito = num % 10
    numInvertido += str(digito)
    num //= 10
    
print("El número invertido es:", numInvertido)