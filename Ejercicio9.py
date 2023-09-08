fecha_nacimiento = input("Por favor, ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")

dia, mes, anio = fecha_nacimiento.split('/')

if len(dia) == 1:
    dia = '0' + dia

if len(mes) == 1:
    mes = '0' + mes

print("Su día de nacimiento es:", dia)
print("Su mes de nacimiento es:", mes)
print("Su año de nacimiento es:", anio)
