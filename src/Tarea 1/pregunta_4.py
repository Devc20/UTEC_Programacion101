"""
Realice una función que reciba como parámetro una frase o palabra y un número entero
positivo n, y la función devuelva la frase luego de haber aplicado n rotaciones en sentido
antihorario a los caracteres de la frase.
"""

def pregunta_4(frase: str, numero_rotaciones: int) -> str:
    lista_frase = list(frase)
    lista_nueva = lista_frase[-len(lista_frase)+numero_rotaciones:]

    for i in range(0, numero_rotaciones):
        lista_nueva.append(lista_frase[i])

    palabra_concatenada = "".join(lista_nueva)

    return palabra_concatenada

print(pregunta_4("Lo que embellece el desierto", 10))