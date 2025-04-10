# @file ejercicio1Funciones.py
#
# @brief Funciones para el calculo de la factura de un producto.
# @date 10/04/2025

import os
os.system("cls")

"""
 @brief Funcion para el ingreso de un importe de un producto.

 @return importeProducto Monto del producto.
"""
def ingresarImporteProducto():
    importeProducto = float(input("Ingrese el monto del producto: "))
    return importeProducto

"""
 @brief Funcion para el ingreso de la cantidad de un producto.

 @return cantidad Cantidad del producto.
"""
def ingresarCantidadProducto():
    cantidad = int(input("Ingrese la cantidad del producto: "))
    return cantidad

"""
 @brief Funcion para el calculo del monto del IVA.

 @param monto Monto del producto.
 
 @return montoIVA Monto del IVA.
"""
def calculoIVA(monto):
    iva = monto*(0.21)
    return iva

"""
 @brief Funcion para el calculo del total de la factura de un producto.

 @param subtotalFactura Subtotal de la factura.
 @param montoIVA Monto del IVA.
 
 @return totalFactura Total de la factura.
"""
def calculoTotalFactura(subtotalFactura, montoIVA):
    totalFactura = subtotalFactura + montoIVA
    return totalFactura

"""
 @brief Funcion para el mostrar la factura de la compra.
 
 @param apellido Nombre del cliente.
 @param dni DNI del cliente.
 @param localidad Localidad del cliente.
 @param subtotalFactura Subtotal de la factura.
 @param montoIVA Monto del IVA.
 @param totalFactura Total de la factura.

 @return None
"""
def mostrarFactura(apellido, dni, localidad, subtotalFactura, montoIVA, totalFactura):
    print("\n--------------------------------------------")
    print(f"Apellido del cliente: {apellido}")
    print(f"DNI del cliente: {dni}")
    print(f"Localidad del cliente: {localidad}")
    print()
    print(f"Subtotal: {subtotalFactura}")
    print(f"IVA: {montoIVA}")
    print(f"Total: {totalFactura}")
    print("--------------------------------------------")


## @brief Programa principal: solicita datos del cliente y productos, calcula la factura y la muestra.

# Para el cliente.
print("\nIngrese los datos del cliente: ")
apellido = input("Ingrese el apellido del cliente: ")
dni = int(input("Ingrese el DNI del cliente: "))
localidad = input("Ingrese la localidad del cliente: ")

# Para el producto 1.
print("\nIngrese los datos del producto 1: ")
importeProducto1 = ingresarImporteProducto()
cantidadProducto1 = ingresarCantidadProducto()

# Para el producto 2
print("\nIngrese los datos del producto 2: ")
importeProducto2 = ingresarImporteProducto()
cantidadProducto2 = ingresarCantidadProducto()

# Calculo monto SIN INCLUIR IVA
subtotalFactura = importeProducto1*cantidadProducto1 + importeProducto2*cantidadProducto2

# Calculo monto CON IVA
montoIVA = calculoIVA(subtotalFactura)

# Calculo monto TOTAL
totalFactura = calculoTotalFactura(subtotalFactura, montoIVA)

# Imprimiendo la factura
mostrarFactura(apellido, dni, localidad, subtotalFactura, montoIVA, totalFactura)