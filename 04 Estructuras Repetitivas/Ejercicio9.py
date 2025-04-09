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