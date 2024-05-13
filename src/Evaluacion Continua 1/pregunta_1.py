"""El centro de análisis de datos de LATAM, cuenta con la siguiente información.
Se sabe que la aereolina ofrece al día como máximo 25 vuelos de Lima a Cusco, y otros
25 vuelos como máximo de Cusco a Lima.
La capacidad de los aviones es de 180 pasajeros si el vuelo está totalmente lleno.
Cada vuelo obtiene el permiso para volar siempre y cuando el vuelo este totalmente
lleno.
Proximamente entrará en vigencia un decreto que indica que la aereolinea tendría que
pagar un importe de 22.5 soles por cada pasajero que transporte ya sea de Lima a Cusco
o de Cusco a Lima, sin importar el importe del precio del boleto que el pasajero haya
pagago y sin importar si lleva equipaje o no. Por otro, lado se sabe que los vuelos programados
no siempre salen por factores relacionado al clima, por ejemplo puede haber
mucha lluvia o puede habe mucho viento y en ese caso algunos vuelos pueden ser cancelados.
Se solicita que realice una función que reciba como parámetro la cantidad de vuelos de
Lima a Cusco y la cantidad de vuelos de Cusco a Lima, que efectivamente se realizadon
y la función calcule la cantidad de soles que LATAM tendría que pagar por transportar
pasajeros en ese día."""

def pregunta_1(numVuelosDeIDa: int, numVuelosDeRegreso: int) -> float:
    cantidad = numVuelosDeIDa + numVuelosDeRegreso
    costoPorPasajero = 22.5
    capacidadMaxima = 180
    monto = capacidadMaxima*costoPorPasajero*cantidad
    return monto