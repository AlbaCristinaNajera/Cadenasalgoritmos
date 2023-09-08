Nombre_usuario = input("Por favor ingrese su nombre: ")

nombre = Nombre_usuario.lower()
letras = Nombre_usuario.replace(" " , "")
contar= len(letras)


print(nombre, "tiene", contar , "letras")