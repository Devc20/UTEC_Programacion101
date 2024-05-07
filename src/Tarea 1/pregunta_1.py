"""
El profesor del curso de ingl´es ha aplicado a sus alumnos una sola pregunta como examen
final. La pregunta tiene un puntaje m´aximo de 9 puntos, pero de acuerdo con la respuesta de
los alumnos, el puntaje que se asigna a la respuesta puede ser desde 0 hasta 9. El asistente
de c´atedra ha anotado los puntajes de todos los alumnos que rindieron el examen, formando
una cadena de caracteres, donde cada casillero de la cadena representa el puntaje de un
alumno.
Considerando esta información, se pide que realice una función que reciba como parámetro
la cadena, y que la función halle la nota promedio del salón, expresada con un máximo de
dos cifras decimales, es decir, devuelve un número float. Por otro lado, considere que el
tamaño de la cadena que procesará la función puede variar, ya que depende de la cantidad
de alumnos que rindieron la prueba, sin embargo, este es un dato que la función puede calcular
internamente a partir del string.

"""
cadena = input("Por favor ingrese la cadena: ")

def pregunta_1(cadena: str) -> float:
    cadena_lista = list(cadena)
    promedio = 0
    suma = 0
    for i in range(len(cadena)):
        suma += int(cadena_lista[i])
    promedio = suma/len(cadena)
    return round(promedio, 2)
print(pregunta_1(cadena))




