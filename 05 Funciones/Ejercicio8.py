# Ejercicio 8

def calcular_imc(peso, altura):
    if isinstance(peso, str) or isinstance(altura, str):
        return print("Error: El peso y la altura no pueden ser strings")
    if peso <= 0 or altura <= 0:
        return print("Error: El peso y la altura deben ser mayores que cero")
    imc = round(peso / (altura ** 2), 2)
    return print(f"Tu IMC es: {imc}")

# calcular_imc(60, 1.52)