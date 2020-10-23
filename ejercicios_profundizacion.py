#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Sebastian Volpe"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    numero_1 = int(input('Ingrese el primer número:\n'))
    numero_2 = int(input('Ingrese el Segundo número:\n'))
    diferencia = numero_1 - numero_2
    print("La diferencia de estos numeros es:", diferencia)
    
    if diferencia > 0:
        print("El resultado es positivo")
    elif diferencia < 0:
        print("El resultado es negativo")
    else:
        print("El resultado es 0")


def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    numero_1 = int(input('Ingrese el primer número:\n'))
    if (numero_1 % 2) == 0:
        print("Es un numero par")
    else:
        print("Es un numero impar")

    numero_2 = int(input('Ingrese el segundo número:\n'))
    if (numero_2 % 2) == 0:
        print("Es un numero par")
    else:
        print("Es un numero impar")

    numero_3 = int(input('Ingrese el Tercer número:\n'))
    if (numero_3 % 2) == 0:
        print("Es un numero par")
    else:
        print("Es un numero impar")


def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    numero_1 = int(input('Ingrese el primer número:'))
    numero_2 = int(input('Ingrese el Sgundo número:'))

    print("Ingrese operacion a realizar:\n+ - *\n/ **")
    calcular = input()

    if calcular == "+":
        print("La suma es= ", numero_1 + numero_2)
    elif calcular == "-":
        print("La resta es= ", numero_1 - numero_2)
    elif calcular == "*":
        print("La multipliacion es= ", numero_1 * numero_2)
    elif calcular == "/":
        print("La division es= ", numero_1 / numero_2)
    elif calcular == "**":
        print("El exponente es= ", numero_1 ** numero_2)
    else:
        print("Usted no ha ingresado un operador!")
    



def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor
    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    palabra_1 = str(input("Ingrese la primera palabra:\n"))
    palabra_2 = str(input("Ingrese la Segunda palabra:\n"))
    palabra_3 = str(input("Ingrese la Tercera palabra:\n"))

    longitud_1 = len(palabra_1)
    longitud_2 = len(palabra_2)
    longitud_3 = len(palabra_3)
    
    print("Ingresar 1:(ordenar alfabeticamente) o 2:(Ordenar por cantidad de letras)")
    orden = int(input())

    # Intente usar el operador ">" como decia el enunciado y no usar otra funcion
    # Creo que funciona pero no se si era lo solicitado!
    if orden == 1:
        if (palabra_1 > palabra_2) and (palabra_1 > palabra_3):
            if palabra_2 > palabra_3:
                print("Ordenados de Mayor a menor:", palabra_1, palabra_2, palabra_3)
            else:
                print("Ordenados de Mayor a menor:", palabra_1, palabra_3, palabra_2)
        elif (palabra_2 > palabra_1) and (palabra_2 > palabra_3):
            if palabra_1 > palabra_3:
                print("Ordenados de Mayor a menor:" ,palabra_2, palabra_1, palabra_3)
            else:
                print("Ordenados de Mayor a menor:" ,palabra_2, palabra_3, palabra_1)
        elif (palabra_3 > palabra_1) and (palabra_3 > palabra_2):
            if palabra_2 > palabra_1:
                print("Ordenados de Mayor a menor:" ,palabra_3, palabra_2, palabra_1)
            else:
                print("Ordenados de Mayor a menor:" ,palabra_3, palabra_1, palabra_2)
    else:
        if orden == 2:
            if (longitud_1 > longitud_2) and (longitud_1 > longitud_3):
                if longitud_2 > longitud_3:
                    print("Ordenados por Cantidad de Letras:", longitud_1, longitud_2, longitud_3)
                else:
                    print("Ordenados por Cantidad de Letras:", longitud_1, longitud_3, longitud_2)
            elif (longitud_2 > longitud_1) and (longitud_2 > longitud_3):
                if longitud_1 > longitud_3:
                    print("Ordenados por Cantidad de Letras:" ,longitud_2, longitud_1, longitud_3)
                else:
                    print("Ordenados por Cantidad de Letras:" ,longitud_2, longitud_3, longitud_1)
            elif (longitud_3 > longitud_1) and (longitud_3 > longitud_2):
                if longitud_2 > longitud_1:
                    print("Ordenados por Cantidad de Letras:" ,longitud_3, longitud_2, longitud_1)
                else:
                    print("Ordenados por Cantidad de Letras:" ,longitud_3, longitud_1, longitud_2) 


def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

    temperatura_1 = float(input('Ingrese primer Valor Temperatura:\n'))
    temperatura_2 = float(input('Ingrese Segundo Valor Temperatura:\n'))
    temperatura_3 = float(input('Ingrese Tercer Valor Temperatura:\n'))

    # Temperatura maxima
    if (temperatura_1 > temperatura_2) and (temperatura_1 > temperatura_3):
        print("Temperatura mayor ingresada:", temperatura_1)
    elif (temperatura_2 > temperatura_1) and (temperatura_2 > temperatura_3):
        print("Temperatura mayor ingresada:", temperatura_2)
    else:
        print("Temperatura mayor ingresada:", temperatura_3)

    # Temperatura Minima
    if (temperatura_1 < temperatura_2) and (temperatura_1 < temperatura_3):
        print("Temperatura menor ingresada:", temperatura_1)
    elif (temperatura_2 < temperatura_1) and (temperatura_2 < temperatura_3):
        print("Temperatura menor ingresada:", temperatura_2)
    else:
        print("Temperatura menor ingresada:", temperatura_3)

    # Temperatura promedio
    promedio = float((temperatura_1 + temperatura_2 + temperatura_3) / 3)
    print("El promedio de las tres temperatura es:", promedio)
    
    

    


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    #ej5()
