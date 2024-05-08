cadena = input("Ingresa una cadena: ")

if cadena[-1].isnumeric():
    primer_numero = ""
    for indice, caracter in enumerate(cadena):
        if caracter.isnumeric():
            primer_numero = indice
            break
    
    numero = ""
    palabra_sola =""
    for indice, caracter in enumerate(cadena):
        if indice >= primer_numero:
            numero += caracter
        else:
            palabra_sola += caracter

    numero = int(numero)
    numero += 1

    cadena = palabra_sola + str(numero)

else:
    cadena += "1"



print(cadena)