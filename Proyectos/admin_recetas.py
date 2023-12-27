#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : J.Carlos
# Created Date: 19/12/2023
# version ='0.5'
# ---------------------------------------------------------------------------

import os
from pathlib import Path
from os import system


def inicio():
    ruta = Path(os.getcwd(), "Recetas")
    print("-" * 45)
    print("Hola, bienvenido a tu recetario.")
    print(f"La ruta actual del recetarío es: {ruta}")
    print(f"El número actual de recetas es: {total_recetas(ruta)}")
    print("-" * 45)
    opcion = 'x'
    while not opcion.isnumeric() or int(opcion) not in range(1, 7) and opcion != 6:
        print("""
                ------------
                | Opciones |
                ------------    
                [1] Leer receta
                [2] Crear receta
                [3] Crear categoría
                [4] Eliminar receta
                [5] Eliminar categoría
                [6] Cerrar
            """)
        opcion = input("Selecciona una opción numérica de 1 - 6: ")
        # limpiar_consola()
    if opcion == '1':
        limpiar_consola()
        leer_receta(ruta)
        inicio()
    elif opcion == '2':
        limpiar_consola()
        crear_receta(ruta)
        inicio()
    elif opcion == '3':
        limpiar_consola()
        crear_categoria(ruta)
        inicio()
    elif opcion == '4':
        limpiar_consola()
        eliminar_receta(ruta)
        inicio()
    elif opcion == '5':
        limpiar_consola()
        eliminar_categoria(ruta)
        inicio()
    elif opcion == '6':
        limpiar_consola()
        print("Cerrando programa... ")


def listar_categorias(ruta):
    opcion = 'x'
    categorias = os.listdir(ruta)
    while not opcion.isnumeric() or int(opcion) not in range(1, len(categorias) + 1):
        contador = 1
        for categoria in categorias:
            print(f"[{contador}] - {categoria}")
            contador += 1
        opcion = input("Selecciona el número de categoría: ")
    return categorias[(int(opcion) - 1)]


def crear_categoria(ruta):
    ruta = Path(ruta, input("Introduce un nombre de catagoría: "))
    os.makedirs(ruta)


def eliminar_categoria(ruta):
    print("Eliminar categoría\n")
    ruta = Path(ruta, listar_categorias(ruta))
    os.rmdir(ruta)


def listar_recetas(ruta, categoria):
    opcion = 'x'
    directorio = Path(ruta, categoria)
    while not opcion.isnumeric() or int(opcion) not in range(1, total_recetas(ruta)):
        contador = 1
        for archivo in directorio.glob("**/*.txt"):
            print(f"[{contador}] {archivo.stem}")
            contador += 1
        opcion = input("Indica el número de receta: ")
    ruta = Path(ruta, categoria, os.listdir(directorio)[int(opcion) - 1])
    return ruta


def leer_receta(ruta):
    ruta_receta = Path(listar_recetas(ruta, listar_categorias(ruta)))
    archivo = open(ruta_receta)
    print(archivo.read())  # Pinta el contenido del fichero
    archivo.close()


def crear_receta(ruta):
    categoria = listar_categorias(ruta)
    nueva_receta = input("Nombre de la receta a crear: ") + '.txt'
    Path(ruta, categoria)
    open(nueva_receta, 'x')
    listar_categorias()


def eliminar_receta(ruta):
    os.remove(Path(listar_recetas(ruta, listar_categorias(ruta))))


def total_recetas(ruta):
    cantidad = 0
    for path in Path(ruta).glob("**/*.txt"):
        cantidad += 1
    return cantidad


def limpiar_consola():
    return system("cls" if os.name in ("nt", "dos") else "clear")

inicio()