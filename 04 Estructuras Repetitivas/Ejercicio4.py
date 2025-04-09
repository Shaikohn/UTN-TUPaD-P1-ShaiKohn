# Ejercicio 4

num = int(input("Ingrese un número entero positivo: "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingrese un número entero positivo: "))

print("El total acumulado es:", suma)