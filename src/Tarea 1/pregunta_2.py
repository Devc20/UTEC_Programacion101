"""
Realice una función que reciba como parámetro una frase y una palabra, y la función indique
si con las letras que contiene la frase, se puede formar la palabra. Note que para formar la
palabra, se puede usar más de una vez una letra de la frase. La frase y la palabra pueden
contener letras en mayúsculas, minúsculas o una combinación de ambos tipos de letras, y
debe tratarlas como si fueran iguales, es decir, no hará distinción entre letras mayúsculas y
minúsculas. La función devolvería un dato de tipo cadena con la frase ”Se puede formar la
palabra” o ”No se puede formar la palabra”.
"""

def pregunta_2(cadena: str, palabra: str) -> str:
    cadena = cadena.upper()
    palabra = palabra.upper()
    lista_palabra = list(palabra)
    for i in range(len(palabra)):
        if lista_palabra[i] in cadena:
            continue
        else:
            return "No se puede formar la palabra"
    return "Se puede formar la palabra"


print(pregunta_2("HABLAS como las personas grandes", "helado"))

