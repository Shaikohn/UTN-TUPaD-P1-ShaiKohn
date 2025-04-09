# Ejercicio 2

cont = 0
num = int(input("Ingrese un número entero positivo: "))

while num >= 1:
    cont += 1
    num //= 10

print("La cantidad de dígitos es:", cont)