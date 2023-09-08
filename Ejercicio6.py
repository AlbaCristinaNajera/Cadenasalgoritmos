frase = input("Por favor ingrese una frase: ")
vocal = input("Por favor ingrese una vocal: ")

if len(vocal) != 1 or vocal.lower() not in 'aeiou':
    print("Por favor, ingrese una única vocal válida (a, e, i, o, u).")
else:
    frase_resaltada = ""
    for letra in frase:
        if letra.lower() == vocal.lower():
            frase_resaltada += vocal.upper()
        else:
            frase_resaltada += letra

    
    print(frase_resaltada)


