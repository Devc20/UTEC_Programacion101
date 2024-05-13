"""Realice una función que reciba como parámetro la magnitud del sismo y la
función devuelva una frase indicando el tipo de sismo"""

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