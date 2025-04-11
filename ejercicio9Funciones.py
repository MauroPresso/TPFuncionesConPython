# @file ejercicio9Funciones.py
#
# @brief Calcula la cantidad de segundos en un tiempo ingresado por el usuario.
# @date 10/04/2025

import os
os.system("cls")

"""
 @brief Funcion para el calculo de la cantidad de segundos en un tiempo ingresado por el usuario.
 
 @param horas: cantidad de horas.
 @param minutos: cantidad de minutos.
 @param segundos: cantidad de segundos.

 @return la cantidad de segundos en un tiempo ingresado por el usuario.
"""
def calcularSegundos(horas, minutos, segundos):
    segundos = horas * 3600 + minutos * 60 + segundos
    return segundos

# @brief Programa principal: calculo de la cantidad de segundos en un tiempo ingresado por el usuario.
# @return 0 si el programa se ejecuto correctamente.

horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))
segundos_totales = calcularSegundos(horas, minutos, segundos)
print("La cantidad de segundos es:", segundos_totales)