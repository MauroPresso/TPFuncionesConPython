# @file ejercicio10incisofFunciones.py
#
# @brief Programa que permite ingresar los datos de un estudiante y calcular el promedio de sus notas en una materia.
# @date 13/04/2025

import os
os.system("cls")

"""
 @brief Calcula el promedio de las notas de un estudiante.

 @param nota1 La primera nota del estudiante.
 @param nota2 La segunda nota del estudiante.
 @param nota3 La tercera nota del estudiante.

 @return El promedio de las notas del estudiante.
"""
def promedioNotas(nota1, nota2, nota3):
    sumaNotas = nota1 + nota2 + nota3
    promedio = sumaNotas / 3
    print(f"El promedio de tus notas es: {promedio}")
    return promedio

"""
 @brief Muestra los datos del estudiante y su promedio.

 @param nombre El nombre del estudiante.
 @param apellido El apellido del estudiante.
 @param materia La materia en la que el estudiante está cursando.
 @param promedio El promedio de las notas del estudiante.

 @return None
"""
def mostrarDatos(nombre, apellido, materia, promedio):
    print("\n-----------------------------------")
    print("Datos del estudiante:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Materia: {materia}")
    print(f"Promedio: {promedio}")
    print("-----------------------------------")


# @brief Programa principal: permite ingresar los datos de un estudiante y calcular el promedio de sus notas en una materia.

nombre = input("Ingrese el nombre del estudiante: ")
apellido = input("Ingrese el apellido del estudiante: ")
materia = input("Ingrese el nombre de la materia: ")
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
promedio = promedioNotas(nota1, nota2, nota3)
mostrarDatos(nombre, apellido, materia, promedio)

