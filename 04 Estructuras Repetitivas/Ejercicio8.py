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