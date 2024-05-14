def pregunta_1(dia: int, mes: int) ->str:
    if ((mes>=1 and mes<=2) or (mes==3 and dia<=20) or (mes==12 and dia>=21)):
        estacion = "Verano"
    if ((mes>=4 and mes<=5) or (mes==3 and dia>=21) or (mes==6 and dia<=21)):
        estacion = "Otonno"
    if ((mes>=7 and mes<= 8) or (mes==6 and dia>=22) or (mes==9 and dia<=22)):
        estacion = "Invierno"
    if ((mes>=10 and mes<=11) or (mes==9 and dia>=23) or (mes==12 and dia<=20)):
        estacion = "Primavera"
    return estacion


def pregunta_2(n1: int, n2: int) -> int:
    if n1 >= n2:
        raise ValueError("n1 menor que n2")
    suma = 0
    for numero in range(n1, n2+1):
        if (numero % 5 == 0 and numero % 7 == 0) or (numero % 3 == 0 and numero % 4 == 0):
            suma += numero
    return suma


def pregunta_3(numero: int) -> int:
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma

      
def pregunta_4(numeroDeTerminos: int) -> int:
    suma_cubos = 0
    for i in range(1, numeroDeTerminos+1):
        suma_cubos += i**3
    return suma_cubos
