# Ejercicio 4

edadUsuario = int(input("Ingrese su edad: "))
if edadUsuario < 12:
    print("El usuario es un niño/a.")
elif edadUsuario >= 12 and edadUsuario < 18:
    print("El usuario es un adolescente.")
elif edadUsuario >= 18 and edadUsuario < 30:
    print("El usuario es un/a adulto/a joven.")
elif edadUsuario >= 30:
    print("El usuario es un/a adulto/a.")