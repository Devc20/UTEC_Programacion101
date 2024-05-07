def pregunta_1(cadena: str) -> float:
    cadena_lista = list(cadena)
    promedio = 0
    suma = 0
    for i in range(len(cadena)):
        suma += int(cadena_lista[i])
    promedio = suma / len(cadena)
    return round(promedio, 2)


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


def pregunta_3(numero: int) -> list:
    lista = []
    lista.append(numero)
    while numero != 1:
        if numero % 2 == 0:
            numero = int(numero / 2)
            lista.append(numero)
        elif numero % 2 != 0 and numero != 1:
            numero = numero * 3 + 1
            lista.append(numero)

    return lista


def pregunta_4(frase: str, numero_rotaciones: int) -> str:
    lista_frase = list(frase)
    lista_nueva = lista_frase[-len(lista_frase) + numero_rotaciones:]

    for i in range(0, numero_rotaciones):
        lista_nueva.append(lista_frase[i])

    palabra_concatenada = "".join(lista_nueva)

    return palabra_concatenada
