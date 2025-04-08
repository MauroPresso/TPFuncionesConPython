## @file ejercicio1Funciones.py
import os
os.system("cls")

def ingresarImporteProducto():
    importeProducto = float(input("Ingrese el monto del producto: "))
    return importeProducto


def ingresarCantidadProducto():
    cantidad = int(input("Ingrese la cantidad del producto: "))
    return cantidad

def calculoIVA(monto):
    iva = monto*(0.21)
    return iva

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


## Main program
print()
print("Ingrese los datos del cliente: ")
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

# IVA
montoIVA = calculoIVA(subtotalFactura)

# Total de la factura
totalFactura = subtotalFactura + montoIVA

# Imprimiendo la factura
mostrarFactura(apellido, dni, localidad, subtotalFactura, montoIVA, totalFactura)