# Ejercicio 5

def frase():
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    palabras_unicas = set(palabras)
    
    print(f"Palabras únicas: {', '.join(palabras_unicas)}")
    diccionario_palabras = {palabra: palabras.count(palabra) for palabra in palabras_unicas}
    print("Cantidad de veces que aparece cada palabra:")
    for palabra, cantidad in diccionario_palabras.items():
        print(f"{palabra}: {cantidad} vez/veces")

frase()