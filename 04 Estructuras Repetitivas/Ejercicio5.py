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