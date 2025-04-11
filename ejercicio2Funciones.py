# @file ejercicio1Funciones.py
#
# @brief Funciones para el calculo del descuento, el vuelto y el total a abonar.
# @date 10/04/2025

import os
os.system("cls")

"""
 @brief Función que calcula el descuento del 5%.

 @param totalFactura: El total de la factura.

 @return El descuento del 5%.
"""
def calcularDescuentoDel5porCiento(totalFactura):
    descuento = totalFactura*0.05
    return descuento

"""
 @brief Función que calcula el total a abonar después del descuento.

 @param totalFactura: El total de la factura.
 @param descuento: El descuento del 5%.

 @return El total a abonar después del descuento.
"""
def calcularTotalAbonar(totalFactura, descuento):
    totalAbonar = totalFactura - descuento
    return totalAbonar


"""
 @brief Función que calcula el vuelto que debe darle al cliente.

 @param montoPago: El monto con el que pagó el cliente.
 @param totalFactura: El total de la factura.

 @return El vuelto que debe darle al cliente.
"""
def calcularVuelto(montoPago, totalFactura):
    vuelto = montoPago - totalFactura
    return vuelto

"""
 @brief Función que muestra los resultados del cálculo.

 @param totalFactura: El total de la factura.
 @param descuento: El descuento del 5%.
 @param totalAbonar: El total a abonar después del descuento.
 @param montoPago: El monto con el que pagó el cliente.
 @param vuelto: El vuelto que debe darle al cliente.

 @return None
"""
def mostrarResultados(totalFactura, descuento, totalAbonar, montoPago, vuelto):
    print("\n--------------------------------------------")
    print("Total de la factura: ", totalFactura)
    print("Descuento: ", descuento)
    print("Total a abonar: ", totalAbonar)
    print("Monto con el que pagó el cliente: ", montoPago)
    print("Vuelto: ", vuelto)
    print("--------------------------------------------")

# @brief Programa principal: Solicita al usuario el monto total de la factura y el monto con el que pagó el cliente. 
# Calcula el descuento y el vuelto que debe darle al cliente.
# @return None

totalFactura = float(input("Ingrese el monto total de la factura: "))

descuento = calcularDescuentoDel5porCiento(totalFactura)
totalAbonar = calcularTotalAbonar(totalFactura, descuento)
montoPago = float(input("Ingrese el monto con el que pagó el cliente: "))
vuelto = calcularVuelto(montoPago, totalFactura)

mostrarResultados(totalFactura, descuento, totalAbonar, montoPago, vuelto)