# Ejercicio 8

productos = {
    'galletitas': 45,
    'alfajores': 50,
    'chocolates': 30,
    'caramelos': 140,
    'chicles': 80,
}

def menu_productos():
    print("1. Consultar el stock de un producto")
    print("2. Agregar unidades al stock de un producto")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == '1':
        consultar_stock()
    elif opcion == '2':
        agregar_unidades()
    elif opcion == '3':
        agregar_nuevo_producto()
    elif opcion == '4':
        print("Saliendo del programa.")
        return
    else:
        print("Opción no válida. Intente nuevamente.")

def consultar_stock():
    producto = input("Ingrese el nombre del producto a consultar: ").lower()
    if producto in productos:
        print(f"El stock de {producto} es {productos[producto]} unidades.")
    else:
        print(f"El producto {producto} no existe en el stock.")

def agregar_unidades():
    producto = input("Ingrese el nombre del producto al que desea agregar unidades: ").lower()
    if producto in productos:
        unidades = int(input(f"Ingrese la cantidad de unidades a agregar al stock de {producto}: "))
        productos[producto] += unidades
        print(f"Se han agregado {unidades} unidades al stock de {producto}. Nuevo stock: {productos[producto]} unidades.")
    else:
        print(f"El producto {producto} no existe en el stock.")

def agregar_nuevo_producto():
    producto = input("Ingrese el nombre del nuevo producto: ").lower()
    if producto not in productos:
        unidades = int(input(f"Ingrese la cantidad de unidades del nuevo producto {producto}: "))
        productos[producto] = unidades
        print(f"Producto {producto} agregado con {unidades} unidades al stock.")
    else:
        print(f"El producto {producto} ya existe en el stock.")

menu_productos()