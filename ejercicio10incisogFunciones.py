# @file ejercicio10incisogFunciones.py
#
# @brief Programa que permite ingresar los datos de un cliente y calcular el total de su factura.
# @date 13/04/2025

import os
os.system("cls")

"""
 @brief Función que permite calcular el importe de un producto

 @param cantidad: Cantidad de productos
 @param precio: Precio del producto

 @return importe del producto
"""
def calcularImporteProducto(cantidad, precio):
    importe = cantidad * precio
    return importe

"""
 @brief Función que permite calcular el IVA del producto

 @param importe: importe del producto

 @return IVA del producto
"""
def calcularIVAdel21porCiento(totalImporte):
    IVA = totalImporte * 0.21
    return IVA

"""
 @brief Función que permite calcular el descuento del producto

 @param importe importe del producto

 @return descuento del producto
"""
def calcularDescuentoDel5porCiento(importe):
    descuento = importe * 0.05
    return descuento

"""
 @brief Función que permite calcular el total del producto

 @param importe: importe del producto
 @param IVA: IVA del producto
 @param descuento: descuento del producto

 @return total del producto
"""
def calcularTotal(importe, IVA, descuento):
    total = importe + IVA - descuento
    return total

"""
 @brief Función que permite mostrar el total del producto

 @param apellido: Apellido del cliente
 @param DNI: DNI del cliente
 @param importe: importe del producto
 @param IVA: IVA del producto
 @param descuento: descuento del producto
 @param total: total del producto

 @return None
"""
def mostrarFactura(apellido, DNI, importe, IVA, descuento, total):
    print("\n------------Factura del cliente------------")
    print("Apellido:", apellido)
    print("DNI:", DNI)
    print()
    print("Subtotal:", importe)
    print("IVA:", IVA)
    print("Descuento:", descuento)
    print()
    print("TOTAL:", total)
    print("------------------------------------------")

# @brief Programa principal: permite ingresar los datos de un cliente y calcular el total de su factura.
# Ingresando los datos del cliente
apellido = input("Ingrese el apellido: ")
DNI = int(input("Ingrese el DNI: "))


# Calculando el IMPORTE de cada producto (Se sabe que son 3 productos)
print()
precio1 = float(input("Ingrese el PRECIO del producto 1: "))
cant1 = int(input("Ingrese la CANTIDAD del producto 1: "))
importe1 = calcularImporteProducto(cant1, precio1)
print()
precio2 = float(input("Ingrese el PRECIO del producto 2: "))
cant2 = int(input("Ingrese la CANTIDAD del producto 2: "))
importe2 = calcularImporteProducto(cant2, precio2)
print()
precio3 = float(input("Ingrese el PRECIO del producto 3: "))
cant3 = int(input("Ingrese la CANTIDAD del producto 3: "))
importe3 = calcularImporteProducto(cant3, precio3)
print()

# Calculando el TOTAL de la compra
importe = importe1 + importe2 + importe3

# Calculando el IVA del TOTAL de la compra
IVA = calcularIVAdel21porCiento(importe)

# Calculando el descuento del 5% del TOTAL de la compra
descuento = calcularDescuentoDel5porCiento(importe)

# Calculando el total de la factura.
totalFactura = calcularTotal(importe, IVA, descuento)

# Mostrando los datos de la factura
mostrarFactura(apellido, DNI, importe, IVA, descuento, totalFactura)

