#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Sebastian Volpe"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda
    if numero_1 > numero_2:
        print("El numero mayor es:", numero_1)
    elif numero_1 == numero_2:
        print("Son los dos numeros iguales")
    else:
        print("El numero mayor es:", numero_2)

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso
    if numero_1 > 0:
        print("El numero 1 es positivo")
    elif numero_1 < 0:
        print("El numero 1 es Negativo")
    else:
        print("El numero 1 es = 0")

    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición
    if (numero_1 > 0 and numero_1 < 100):
        print("Cumple con la condicion es mayor a 0 y menor que 100")
    else:
        print("No cumple con la condicion")

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición
    if (numero_1 < 10) or (numero_2 > -2):
        print("Cumple Al menos cun una condicion")
    else:
        print("No cumple ninguna condicion")


def ej2():
    # Ejemplos variables de texto
    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    if texto_1 < texto_2:
        print(texto_1, "va primero en el diccionario")
    else:
        print(texto_2, "va primero en el diccionario")

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    cantidad_1 = len(texto_1)
    cantidad_2 = len(texto_2)
    if cantidad_1 > cantidad_2:
        print(texto_1, "tiene mas letras")
    elif cantidad_1 == cantidad_2:
        print("Tienen la misma cantidad de letras")
    else:
        print(texto_2, "tiene mas letra")

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    primera_letra_1 = texto_1[0]
    primera_letra_2 = texto_2[0]

    if primera_letra_1 > primera_letra_2:
        print(texto_1, "La primera letra es mayor")
    else:
        print(texto_2, "La primera letra es mayor")

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    if copia_texto_1 == texto_1:
        print("Son iguales las palabras")
    else:
        print("Son palabras distintas")

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
    if copia_texto_1 != texto_2:
        print("Son distintas")
    else:
        print("Son iguales")


def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 5
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"
    if (numero_1 > 5):
        if (numero_2 > 0):
            print("Resp=1")
        else:
            print("resp=2")
    else:
        if numero_2 > 5:
            print("Resp=3")
        else:
            print("Resp=4")

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F
    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados
    if puntaje >= 90:
        print("Su calificacion es A", puntaje)
    else:
        if puntaje >= 80:
            print("Su calificacion es B", puntaje)
        else:
            if puntaje >= 70:
                print("Su calificacion es C", puntaje)
            else:
                if puntaje >= 60:
                    print("Su calificacion es D", puntaje)
                else:
                    if puntaje < 60:
                        print("Su calificacion es F", puntaje)



def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda
    if texto_1 > texto_2:
        print(texto_1, "Es mayor alfabeticamente")
    else:
        print(texto_2, "Es mayor alfabeticamente")

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    numero_1 = int(texto_1)
    numero_2 = int(texto_2)

    if numero_1 > numero_2:
        print(numero_1, "Es mayor")
    else:
        print(numero_2, "Es mayor")

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
