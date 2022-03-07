'''
Ejercicio 2
Simulador de Hacienda.
Cree un programa que permita:
1- Registrar un vendedor  en un diccionario co llave el ID del
vendedor que contenga:
1. Nombre del vendedor
2. Teléfono.
2- Registrar ventas.
Permita un diccionario como llave ID del vendedor registrar facturas de ventas de un
vendedor, donde se registra una clase factura el cual debe detallar.
-Id vendedor
-Fecha factura
-Monto:
-Monto IVA. :
-Monto Total: Monto + Monto IVA
3- Imprimir Ventas:
Imprimir las ventas registradas de un vendedor que se busca por el ID
- Nombre del vendedor.
- fecha factura.
- monto total.
4- Guardar los datos:
Guardar los datos del vendedor en un archivo con nombre “Vendedores.bin”
Guardar los datos de facturas en un archivo con nombre “Facturas.bin”
'''
from clases_ej2.vendedores import *
from clases_ej2.facturas import *
from clases_ej2.hacienda import *

prueba = Hacienda()
prueba.correr_hacienda()

