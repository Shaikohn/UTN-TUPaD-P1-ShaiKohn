# Ejercicio 7

num = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(0, num + 1):
    suma += i

print("La suma de los números comprendidos entre 0 y", num, "es:", suma)