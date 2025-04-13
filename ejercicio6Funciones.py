# @file ejercicio6Funciones.py
#
# @brief Programa que permite ingresar los datos de una persona: Legajo, Apellido, Nombre, Cantidad de horas normales, cantidad de horas extras.
# @date 13/04/2025

import os
os.system("cls")


"""
 @brief Función que permite calcular el pago correspondiente a la persona según sus horas normales y horas extras.

 @param horasNormales la cantidad de horas normales trabajadas.
 @param horasExtras la cantidad de horas extras trabajadas.

 @return el pago total del legajo.
"""
def calcularPago(horasNormales, horasExtras):
    pagoNormal = horasNormales * 1500 # La hora normal vale 1500 pesos.
    pagoExtra = horasExtras * (1500 + 1500 * 0.5) # La hora extra vale un 50% más que una hora normal.
    pagoTotal = pagoNormal + pagoExtra
    return pagoTotal

"""
 @brief Función que muestra el recibo de pago correspondiente a la persona.

 @param nombre el nombre de la  persona.
 @param apellido el apellido de la persona.
 @param legajo el legajo de la persona.
 @param pagoTotal el pago total del legajo.
 
 @return none.
"""
def mostrarRecibo(nombre, apellido, legajo, pagoTotal):
    print("\n--------------------------------------")
    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Legajo: ", legajo)
    print("Pago total: ", pagoTotal)
    print("--------------------------------------")

# @brief Programa principal: permite ingresar los datos de una persona: Legajo, Apellido, Nombre, Cantidad de horas normales, cantidad de horas extras.
#Ingresar datos de la persona.
legajo = int(input("Ingrese el legajo: "))
apellido = input("Ingrese el apellido: ")
nombre = input("Ingrese el nombre: ")
horasNormales = int(input("Ingrese la cantidad de horas normales: "))
horasExtras = int(input("Ingrese la cantidad de horas extras: "))
pagoTotal = calcularPago(horasNormales, horasExtras)
mostrarRecibo(nombre, apellido, legajo, pagoTotal)

