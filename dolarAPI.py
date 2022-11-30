#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usar una API para consultar el valor del dólar oficial (compra y venta). Se hará uso de "API Dolar Argentina", cuya documentación se encuentra en:
    https://github.com/Castrogiovanni20/api-dolar-argentina

Según la documentación, la URL para hacer las consultas es:
    https://api-dolar-argentina.herokuapp.com/

La sintaxis para el método GET es:
    GET	/api/dolaroficial	Cotizacion dólar oficial
    GET	/api/dolarblue	    Cotizacion dólar blue
"""

def mostrarMenu():
    print("""   ~ Menú ~
    • 1 - Valor dólar oficial
    • 2 - Valor dólar blue
    • 3 - Salir
    """)

def confirmacion():
    input("~ Presione ENTER para continuar ~")

def mostrarPrecioDolar(dolar='oficial'):
    r = requests.get("https://api-dolar-argentina.herokuapp.com/api/dolar"+dolar)
    if r.status_code != 200:
        print("No es posible acceder a los datos")
        return
    datos = r.json()
    print(f"""      ♦ Valor dólar {dolar} ♦
    Fecha: {datos["fecha"]}
    Compra: {datos["compra"]}
    Venta: {datos["venta"]}""")

############################ Script ####################################
from tabulate import tabulate
import requests, os
while True:
    mostrarMenu()
    opcion = input(">>> ")
    if opcion == '1':
        mostrarPrecioDolar()
        confirmacion()
    elif opcion == '2':
        mostrarPrecioDolar('blue')
        confirmacion()
    elif opcion == '3':
        break
    os.system("cls")
