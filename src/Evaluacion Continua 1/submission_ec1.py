def pregunta_1(numVuelosDeIDa: int, numVuelosDeRegreso: int) -> float:
    cantidad = numVuelosDeIDa + numVuelosDeRegreso
    costoPorPasajero = 22.5
    capacidadMaxima = 180
    monto = capacidadMaxima*costoPorPasajero*cantidad
    return monto


def pregunta_2(anguloEnRadianes: float) -> float:
    anguloEnSexagesimales = anguloEnRadianes * (180 / 3.1415)
    return round(anguloEnSexagesimales, 2)


def pregunta_3(magnitud: float) -> str:
    if magnitud < 2:
        return "El sismo es Micro"
    elif 2 <= magnitud < 3:
        return "El sismo es Muy Menor"
    elif 3 <= magnitud < 4:
        return "El sismo es Menor"
    elif 4 <= magnitud < 5:
        return "El sismo es Ligero"
    elif 5 <= magnitud < 6:
        return "El sismo es Moderado"
    elif 6 <= magnitud < 7:
        return "El sismo es Fuerte"
    elif 7 <= magnitud < 8:
        return "El sismo es Mayor"
    elif 8 <= magnitud < 10:
        return "El sismo es Cataclismo"
    else:
        return "El sismo es Meteorico"


def pregunta_4(peso: float, altura: float) -> str:
    tipoDePeso = peso/altura ** 2
    if tipoDePeso < 18.5:
        return "Ud tiene Bajo Peso"
    elif 18.5 <= tipoDePeso < 25:
        return "Ud tiene un peso normal"
    elif 25 <= tipoDePeso < 30:
        return "Ud tiene Sobrepeso"
    elif 30 <= tipoDePeso < 35:
        return "Ud tiene Obesidad Leve"
    elif 35 <= tipoDePeso < 40:
        return "Ud tiene Obesidad Media"
    else:
        return "Ud tiene Obesidad Morbida"
