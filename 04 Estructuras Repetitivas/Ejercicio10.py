# Ejercicio 10

num = int(input("Ingrese un número entero positivo: "))
numInvertido = ""

while num > 0:
    digito = num % 10
    numInvertido += str(digito)
    num //= 10
    
print("El número invertido es:", numInvertido)