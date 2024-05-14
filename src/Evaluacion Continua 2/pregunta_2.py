def pregunta_2(n1: int, n2: int) -> int:
    if n1 >= n2:
        raise ValueError("n1 menor que n2")
    suma = 0
    for numero in range(n1, n2+1):
        if (numero % 5 == 0 and numero % 7 == 0) or (numero % 3 == 0 and numero % 4 == 0):
            suma += numero
    return suma

