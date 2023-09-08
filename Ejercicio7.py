correo = input("Por favor ingresa tu correo electronico: ")

Usuario, dominio = correo.split("@")

nuevo_nombre = (Usuario + "@ceu.es")

print(nuevo_nombre)

