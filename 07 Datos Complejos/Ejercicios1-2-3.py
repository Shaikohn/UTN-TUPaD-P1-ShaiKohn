# Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

def diccionario_de_frutas1():

    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    print("Diccionario de precios de frutas con nuevas frutas: ", precios_frutas)

# Ejercicio 2

def diccionario_de_frutas2():
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800

    print("Diccionario de precios de frutas actualizados: ", precios_frutas)

# Ejercicio 3
def diccionario_de_frutas3():
    frutas = list(precios_frutas.keys())
    print("Lista de frutas: ", frutas)

diccionario_de_frutas1()
diccionario_de_frutas2()
diccionario_de_frutas3()