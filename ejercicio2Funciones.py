## @file ejercicio1Funciones.py
import os
os.system("cls")

def calcularDescuentoDel5porCiento(totalFactura):
    descuento = totalFactura*0.05
    return descuento

def calcularTotalAbonar(totalFactura, descuento):
    totalAbonar = totalFactura - descuento
    return totalAbonar

def calcularVuelto(montoPago, totalFactura):
    vuelto = montoPago - totalFactura
    return vuelto


## Main program

totalFactura = float(input("Ingrese el monto total de la factura: "))