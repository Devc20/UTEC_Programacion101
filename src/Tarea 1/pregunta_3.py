"""
Realice una función que reciba como parámetro un número entero positivo n y la función
forme una lista con números enteros generados siguiendo las siguientes reglas:
• n se incluye como primer elemento de la lista.
• Si n es par, se divide entre 2 (división entera) y se agrega el resultado a la lista.
• Si n es impar, se multiplica por 3 y se le suma 1, y se agrega el resultado a la lista.
• El algoritmo se repite con el último elemento de la lista, hasta que n sea igual a 1
"""

def pregunta_3(numero: int) -> list:
    lista = []
    lista.append(numero)
    while numero!=1:
        if numero % 2 == 0:
            numero = int(numero/2)
            lista.append(numero)
        elif numero % 2 != 0 & numero != 1:
            numero = numero*3 + 1
            lista.append(numero)

    return lista

print(pregunta_3(20))

