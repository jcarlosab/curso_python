#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : J.Carlos
# Created Date: 19/12/2023
# version ='0.5'
# ---------------------------------------------------------------------------

from pathlib import Path
import os


def inicio():

    while True:
        opcion = int(pintar_menu())
        print(f"Test while {opcion}")
        if opcion == 1:
            leer_receta()
        elif opcion == 2:
            crear_receta()
        elif opcion == 3:
            crear_categoria()
        elif opcion == 4:
            eliminar_receta()
        elif opcion == 5:
            eliminar_categoria()
        elif opcion == 6:
            limpiar_consola()
            print("Cerrando programa... ")
            break


def pintar_menu():
    ruta = Path.home()
    print("Hola, bienvenido a tu recetario.")
    print(f"La ruta actual del recetarío es: {ruta}")
    print(f"El número actual de recetas es: {total_recetas()}")
    print("""
        INDICE
        
        [1] Leer receta
        [2] Crear receta
        [3] Crear categoría
        [4] Eliminar receta
        [5] Eliminar categoría
        [6] Cerrar

    """)
    return input("Selecciona una opción numérica de 1 - 6: ")


def listar_categorias():
    aux = 0
    base = Path("C:\\Recetas")
    categorias = os.listdir(base)
    for categoria in categorias:
        aux += 1
        print(f"[{aux}] {categoria}")
    posicion = int(input("Selecciona el número de categoría: "))
    return categorias[(posicion - 1)]


def crear_categoria():
    ruta = Path("C:\\Recetas", input("Introduce un nombre de catagoría: "))
    os.makedirs(ruta)


def eliminar_categoria():
    print("Eliminar categoría\n")
    ruta = Path("C:\\Recetas\\", listar_categorias())
    os.rmdir(ruta)


def listar_recetas(categoria):
    directorio = Path("C:\\Recetas\\", categoria)
    aux = 0
    for archivo in directorio.glob("**/*.txt"):
        aux += 1
        print(f"[{aux}] {archivo.stem}")
    receta = int(input("Indica el número de receta: "))
    ruta = Path("C:\\Recetas\\", categoria, os.listdir(directorio)[receta])
    print(ruta)
    return ruta


def leer_receta():
    print("TODO")
    limpiar_consola()
    ruta_receta = Path(listar_recetas(listar_categorias()))
    archivo = open(ruta_receta)
    print(archivo.read())  # Pinta el contenido del fichero
    archivo.close()


def crear_receta():
    categoria = listar_categorias()
    nueva_receta = input("Nombre de la receta a crear: ") + '.txt'
    Path("C:\\Recetas\\", categoria)
    open(nueva_receta, 'x')
    listar_categorias()


def eliminar_receta():
    limpiar_consola()
    os.remove(Path(listar_recetas(listar_categorias())))


def total_recetas():
    cantidad = 0
    for path in Path(".").iterdir():
        if path.is_file():
            cantidad += 1
    return cantidad


def limpiar_consola():
    return os.system("cls" if os.name in ("nt", "dos") else "clear")

inicio()