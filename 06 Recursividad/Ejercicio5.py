# Ejercicio 5

def es_palindromo(cadena):
    cadena = cadena.lower()
    if len(cadena) <= 1:
        return True
    else:
        return cadena[0] == cadena[-1] and es_palindromo(cadena[1:-1])
    
# Ejemplo de uso con resultado False:

# print(es_palindromo("Shai"))

# Ejemplo de uso con resultado True:

# print(es_palindromo("Ana"))