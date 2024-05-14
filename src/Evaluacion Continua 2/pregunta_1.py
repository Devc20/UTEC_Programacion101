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

