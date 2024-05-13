"""El sobrepeso es el aumento del peso corporal por encima de un patrón dado.
Los expertos utilizan una fórmula para calcular el Indice de Masa Corportal - IMC,
que calcula el nivel de grasa corporal en relación con el peso y la estatura:

IMC = peso/(masa)^2

En donde:
• El peso: se expresa en kilogramos
• La altura: se expresa en metros

Desarrolle una función que reciba como parámetros: el peso expresado en kilos
y la altura expresada en metros y la función devuelva el Tipo de peso.
El tipo de peso, se determina de acuerdo al valor del índice de la masa corporal."""

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

