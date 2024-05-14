def pregunta_4(numeroDeTerminos: int) -> int:
    suma_cubos = 0
    for i in range(1, numeroDeTerminos+1):
        suma_cubos += i**3
    return suma_cubos
