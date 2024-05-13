"""Realice un función que permita convertir un ángulo expresado en radianes a grados
sexagesimales.
La función recibe como parámetro el valor de un ángulo expresado en radianes y devuelve el
equivalente en grados sexagesimales. Exprese la respuesta utilizando dos cifras
decimales.
Recuerde que 3.1415 radianes equivalen a 180 grados sexagesimales.
. Considere un valor de PI = 3.1415
"""

def pregunta_2(anguloEnRadianes: float) -> float:
    anguloEnSexagesimales = anguloEnRadianes * (180 / 3.1415)
    return round(anguloEnSexagesimales, 2)