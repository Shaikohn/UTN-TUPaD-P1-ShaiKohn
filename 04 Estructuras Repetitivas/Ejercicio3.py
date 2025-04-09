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
    
print("La suma de los números entre", menor, "y", mayor, "excluyendo esos valores es:", suma)