# Ejercicio 10

def invertirPaisesYCapitales():
    paises_capitales = {
        "Argentina": "Buenos Aires",
        "Brasil": "Brasilia",
        "Chile": "Santiago",
        "Colombia": "Bogotá",
        "Perú": "Lima"
    }
    
    # Invertir el diccionario
    capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
    
    print("Diccionario original (Países y sus capitales):")
    print(paises_capitales)
    
    print("\nDiccionario invertido (Capitales y sus países):")
    print(capitales_paises)

invertirPaisesYCapitales()