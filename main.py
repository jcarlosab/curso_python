#Print - print()
print("-------- PRINT --------")
print("Hola Mundo")
print("Hola" + " " + "Mundo")
print("Comillas: \" " + "Barra: \\ " + " \t Tabulador" + "\n Salto linea " )
print(100 + 120)
print("-------- FIN PRINT -------- \n")

#Operadores
print("-------- OPERADORES --------")
print("""Suma: +
Resta: -
Multiplicación: *
División: /
Cociente: //
Resto: %
Potencia: **
Raíz cuadrada: **0.5""")
print("-------- FIN OPERADORES -------- \n")

#Operadores lógicos
print("-------- OPERADORES LOGICOS --------")
print("""Igual a: ==
Diferente a: !=
Mayor que: >
Menor que: <
Mayor o igual que: >=
Menor o igual que: <=
y: and
o: or
no: not""")
print("-------- FIN OPERADORES LOGICOS -------- \n")

#Tipos de datos
print("-------- TIPOS DE DATOS --------")
num1 = 7
num2 = 7.7
text = "Hola"
val = False

print(f"Valor número entero {num1} tipo {type(num1)}")
print(f"Valor número decimal {num2} tipo {type(num2)}")
print(f"Valor texto {text} tipo {type(text)}")
print(f"Valor boolean {val} tipo {type(val)}")
print(f"Conversión número entero {num1} a decimal [float()] {float(num1)} tipo {type(float(num1))}")
print(f"Conversión número decimal {num2} a entero [int()] {int(num2)} tipo {type(int(num2))}")
print("-------- FIN TIPOS DE DATOS -------- \n")

#Formatear cadenas
print("-------- FORMATEAR CADENAS --------")
valor_actual = 99
valor_nuevo = "XX"
print("Valor actual {} nuevo valor {}".format(valor_actual, valor_nuevo))
print(f"Valor actual {valor_actual} nuevo valor {valor_nuevo}")
print("-------- FIN FORMATEAR CADENAS -------- \n")

#Redondeo - round(num, ndigits)
print("-------- REDONDEO --------")
print(f"100/3 = {100/3} redondeo [round()] {round(100/3)}")
print(f"100/3 = {12/7,2} redondeo [round()] {round(12/7,2)}")
print(f"100/3 = {100/3} redondeo [round(num, ndigits)] {round(100/3, 3)}")
print("-------- FIN REDONDEO -------- \n")

#Index - index(value, start, end)
print("-------- INDEX --------")
parrafo = """Utilizamos el método index( ) para explorar strings, ya que
permite hallar el índice de aparición de un caracter o cadena de
caracteres dentro de un texto dado."""
print(parrafo.index("explorar"))
print(parrafo.rindex("explorar"))
print(parrafo[2])
print("-------- FIN INDEX -------- \n")

#Substrings
print("-------- SUBSTRINGS --------")
substrText = "Hola_mundo"
print(f"Substring de substrText[0:4] {substrText[0:4]}")
print(f"Substring de substrText[2::3] {substrText[2::3]}")
print(f"Substring de substrText[::-1] {substrText[::-1]}")
print("-------- FIN SUBSTRINGS -------- \n")

#Metodos Strings
print("-------- METODOS STRINGS --------")
hola_mundo = "Hola mundo"
numeros = "123456"
alfabetico = "abcdefg"
cadena = "Hola \n mundo"
parrafo = "Prueba texto para funcion"
mituple = ("ps1", "ps2", "ps3")
midict = {"nombre":"Jose", "apellidos":"Barros"}

print("----- Análisis -----")
print(f"Método count() | Test cuenta repeticiones de 'Hola' en 'Hola mundo': {hola_mundo.count('Hola')}")
print(f"Método find() | Test buscar 'Hola' en 'Hola mundo': {hola_mundo.find('Hola')}")
print(f"Método find() | Test buscar '123' en 'Hola mundo': {hola_mundo.find('123')}")
print(f"Método rfind() | Test buscar desde el final 'Hola' en 'Hola mundo': {hola_mundo.rfind('Hola')}")
print(f"Método index() | Test buscar 'Hola' en 'Hola mundo': {hola_mundo.index('Hola')}")
print(f"Método rindex() | Test buscar desde el final 'Hola' en 'Hola mundo': {hola_mundo.rindex('Hola')}")
print(f"Método startswith() | Test 'Hola mundo' empieza con 'Hola': {hola_mundo.startswith('Hola')}")
print(f"Método endswith() | Test 'Hola mundo' acaba con 'Hola': {hola_mundo.endswith('Hola')}")
print(f"Método isdigit() | Test dígitos '123456': {numeros.isdigit()}")
print(f"Método isnumeric() | Test números '123456': {numeros.isnumeric()}")
print(f"Método isdecimal() | Test decimales '123456': {numeros.isdecimal()}")
print(f"Método isalnum() | Test alfanuméricos '123456': {numeros.isalnum()}")
print(f"Método isalpha() | Test alfabéticos 'abcdefg': {alfabetico.isalpha()}")
print(f"Método islower() | Test todo minúsculas 'abcdefg': {alfabetico.islower()}")
print(f"Método isupper() | Test todo mayúsculas 'abcdefg': {alfabetico.isupper()}")
print(f"Método isprintable() | Test imprimibles 'abcdefg' (no son caracteres especiales): {alfabetico.isprintable()}")
print(f"Método isspace() | Test espacios '   ' solo espacios: {'  '.isspace()}")
print("--------------------")
print("----- Transformación -----")
print(f"Método capitalize() | Test primera letra en mayúscula 'abcdefg': {alfabetico.capitalize()}")
print(f"Método encode() | Test codifica la cadena con el mapa de caracteres especificado y retorna una instancia del tipo byte 'abcdefg': {alfabetico.encode('utf-8')}")
print(f"Método replace() | Test reemplazar 'mundo' por 'mundo2' en 'Hola mundo': {hola_mundo.replace('mundo', 'mundo2')}")
print(f"Método lower() | Test todo a minúsculas 'ABC': {'ABC'.lower()}")
print(f"Método upper() | Test todo a mayúsculas 'abc': {'abc'.upper()}")
print(f"Método swapcase() | Test cambia minúsculas por mayúsculas 'Ja Ja Ja Ja Ja': {'Ja Ja Ja Ja Ja'.swapcase()}")
print(f"Método strip() | Test quita espacios en blanco izquierda y derecha en '  Hola   ': {'  Hola   '.strip()} FIN")
print(f"Método lstrip() | Test quita espacios en blanco izquierda  en '  Hola   ': {'  Hola   '.lstrip()} FIN")
print(f"Método rstrip() | Test quita espacios en blanco derecha  en '  Hola   ': {'  Hola   '.rstrip()} FIN")
print(f"Método center() | Test alinear al centro 'abc': {'abc'.center(20, ' ')}")
print(f"Método ljust() | Test alinear a la izquierda 'abc': {'abc'.ljust(20, ' ')}")
print(f"Método rjust() | Test alinear a la derecha 'abc': {'abc'.rjust(20, ' ')}")
print("--------------------------")
print("----- Separación y unión -----")
print(f"Método split() | Test separar cadena por defecto ('1 2 3 4 5 6'.split()) '1 2 3 4 5 6': {'1 2 3 4 5 6'.split()}")
print(f"Método split() | Test separar cadena por guiones ('1-2-3'.split('-')) '1-2-3': {'1-2-3'.split('-')}")
print(f"Método splitlines() | Test dividir con salto de linea 'Hola \\n mundo': {cadena.splitlines()}")
print(f"Método partition() | Test partition parte texto en tres partes {parrafo.partition('texto')}")
print(f"Método rpartition() | Test rpartition parte texto en tres partes {parrafo.rpartition('texto')}")
print(f"Método join() | Test join tuple sin separador {''.join(mituple)}")
print(f"Método join() | Test join tuple con separador '#' {'#'.join(mituple)}")
print(f"Método join() | Test join diccionario con separador '#' {'#'.join(midict)}")
print("------------------------------")
print("-------- FIN METODOS STRINGS -------- \n")

#Propiedades Strings
print("-------- PROPIEDADES STRINGS --------")
print(f"Concatenar esta cadena con +" + " cadena nueva")
print(f"Multiplicar linea *3 \n"*3)
print(f"Determinar su longitud con len('Hola mundo'): {len(hola_mundo)}")
print(f"Verificar su contenido  in 'Hola' in 'Hola mundo': {'Hola' in hola_mundo}")
print(f"Verificar su contenido  not in 'Hola' not in 'Hola mundo': {'Hola' not in hola_mundo}")
print("-------- FIN PROPIEDADES STRINGS -------- \n")

#Listas
print("-------- LISTAS --------")
lista_juegos = ["Final Fantasy", "Super Mario", "Sonic"]
lista_consolas = ["PS5", "XBOX", "SW"]
print(f"Listas: juegos -> {lista_juegos} y consolas -> {lista_consolas}")
print(f"Indexado juegos: {lista_juegos[0:2]}")
print(f"Número de elementos consolas: {len(lista_consolas)}")
print(f"Concatenación: {lista_consolas + lista_juegos}")
lista_juegos.append('Death Stranding')
print(f"Método append() | Test append añadir 'Death Stranding' a la lista de juegos {lista_juegos}")
lista_juegos.pop(1)
print(f"Método pop() | Test pop eliminar elemento de la posición 1 {lista_juegos}")
lista_juegos.sort()
print(f"Método sort() | Test sort ordenar lista {lista_juegos}")
lista_juegos.reverse()
print(f"Método reverse() | Test reverse invertir orden de la lista {lista_juegos}")
print("-------- FIN LISTAS -------- \n")

#Diccionarios
mi_diccionario = {"Título":"Final Fantasy", "Genero":"rpg", "Desarrolladora":"SquareEnix"}
print("-------- DICCIONARIOS --------")
print(mi_diccionario)
print(f"Acceso a Desarrolladora en el diccionario {mi_diccionario['Desarrolladora']}")
print("-------- FIN DICCIONARIOS -------- \n")

#Tuples
mi_tuple = (1, "dos", [3.33,"cuatro"], (5.0, 6))
lista_tuple = list(mi_tuple)
a, b, c, d = mi_tuple
print("-------- TUPLES --------")
print(mi_tuple)
print(f"Pintar posición 3: {mi_tuple[2]}")
print(f"Transformar a lista list(mi_tuple): {lista_tuple}")
print(f"Pintar unpacking a: {a}")
print(f"Pintar unpacking b: {b}")
print(f"Pintar unpacking c: {c}")
print(f"Pintar unpacking d: {d}")
print("-------- FIN TUPLES -------- \n")

#Sets
print("-------- SETS --------")
mi_set_a = {1, 2,"tres"}
mi_set_b = {3,"tres"}
print(mi_set_a)
mi_set_a.add(5)
print(f"Método add() | Test add {mi_set_a}")
mi_set_c = mi_set_a.copy()
print(f"Método copy() | Test copy {mi_set_c}")
mi_set_c.clear()
print(f"Método clear() | Test clear {mi_set_c}")

print(f"Método difference() | Test clear {mi_set_c}")

print(f"Método difference_update() | Test clear {mi_set_c}")

print(f"Método discard() | Test clear {mi_set_c}")

print(f"Método intersection() | Test clear {mi_set_c}")

print(f"Método intersection_update() | Test clear {mi_set_c}")

print(f"Método isdisjoint() | Test clear {mi_set_c}")

print(f"Método issubset() | Test clear {mi_set_c}")

print(f"Método issuperset() | Test clear {mi_set_c}")

print(f"Método pop() | Test clear {mi_set_c}")
print(f"Método remove() | Test clear {mi_set_c}")
print(f"Método symmetric_difference() | Test clear {mi_set_c}")
print(f"Método symmetric_difference_update() | Test clear {mi_set_c}")

print(f"Método union() | Test clear {mi_set_c}")

print(f"Método update() | Test clear {mi_set_c}")
print("-------- FIN SETS -------- \n")

#If
print("-------- IF --------")
if 12 > 6:
    print("Test if 12 > 6")
elif false != true and true:
    print("Test elif")
else:
    print("Test else")
print("-------- FIN IF -------- \n")

#Bucles for
print("-------- FOR --------")

for lj in lista_juegos:
    print(f"Valores lista: {lj}")

for t in mi_tuple:
    print(f"Valores tupla: {t}")

for d in mi_diccionario.values():
    print(f"Valores diccionario: {d}")

for k, v in mi_diccionario.items():
    print(f"Clave/Valor diccionario: {k} -> {v}")

print("-------- FIN FOR -------- \n")

#Bucles while
print("-------- WHILE --------")
i = 0
while 2 > i:
    print(f"Test while {i}")
    i = i + 1
else:
    print(f"Final while {i}")

print("-------- FIN WHILE -------- \n")

#range()
print("-------- RANGE --------")
rangos = range(5, 30, 2)
print(f"range(5, 30, 2) {list(rangos)}")
print("-------- FIN RANGE -------- \n")

#enumerate()
print("-------- ENUMERATE --------")
enum1 = enumerate("Final")
enum2 = enumerate("Fantasy", 2)
enum3 = enumerate([4.25, 7, 2])
print(f"enumerate('Final') {list(enum1)}")
print(f"enumerate('Fantasy',2) {list(enum2)}")
for i, n in enum3:
    print(f"Enumerate recorrido con for Indice/Numero {i} -> {n}")
print("-------- FIN ENUMERATE -------- \n")

#Template
print("-------- TEMPLATE --------")
print("-------- FIN TEMPLATE -------- \n")
#Inputs
#print("Texto introducido:" + input("Introduce texto: "))
