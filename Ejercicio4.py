numero_telefonico = input("Por favor ingrese el numero telefonico que contenga prefijo-número-extensión: ")

formato = numero_telefonico.split("-")

if len(formato)==3:
    numero_principal = formato[1]
    print("Número principal:", numero_principal)
