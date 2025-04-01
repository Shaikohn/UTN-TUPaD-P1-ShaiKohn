# Ejercicio 7

frase = input("Ingrese una frase o palabra: ")
if frase.endswith('a') or frase.endswith('A') or frase.endswith('e') or frase.endswith('E') or frase.endswith('i') or frase.endswith('I') or frase.endswith('o') or frase.endswith('O') or frase.endswith('u') or frase.endswith('U'):
    frase = frase + "!"
    print(frase)
else:
    print(frase)