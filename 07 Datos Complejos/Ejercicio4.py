# Ejercicio4

def contactos():
    contactos = {}

    while len(contactos) < 5:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        contactos[nombre] = telefono
    contactoAConsultar = input("Ingrese el nombre del contacto a consultar: ")
    if contactoAConsultar in contactos:
        print(f"El teléfono de {contactoAConsultar} es {contactos[contactoAConsultar]}")
    else:
        print(f"No se encontró el contacto {contactoAConsultar}")

contactos()