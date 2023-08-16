#Print - print()
print("-------- PRINT --------")
print("Hola Mundo")
print("Hola" + " " + "Mundo")
print("Comillas: \" " + "Barra: \\ " + " \t Tabulador" + "\n Salto linea " )
print(100 + 120)
print("-------- FIN PRINT -------- \n")

#Formatear cadenas
print("-------- FORMATEAR CADENAS --------")
valor_actual = 99
valor_nuevo = "XX"
print("Valor actual {} nuevo valor {}".format(valor_actual, valor_nuevo))
print(f"Valor actual {valor_actual} nuevo valor {valor_nuevo}")
print("-------- FIN FORMATEAR CADENAS -------- \n")

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
print(f"Método partition() | Test decimales PENDIENTE")
print(f"Método rpartition() | Test decimales PENDIENTE")
print(f"Método join() | Test decimales PENDIENTE")
print("------------------------------")
print("-------- FIN METODOS STRINGS -------- \n")

#Propiedades Strings
print("-------- PROPIEDADES STRINGS --------")
print(f"Concatenar esta cadena con +" + " cadena nueva")
print(f"Multiplicar linea *3 \n"*3)
print(f"Determinar su longitud con len('Hola mundo'): {len(hola_mundo)}")
print(f"Verificar su contenido  in")
print(f"Verificar su contenido  not in")
print("-------- FIN PROPIEDADES STRINGS --------")

#Listas
print("-------- LISTAS --------")
lista_juegos = ["Final Fantasy", "Super Mario", "Sonic"]
lista_consolas = ["PS5", "XBOX", "SW"]
print(f"Listas: juegos -> {lista_juegos} y consolas -> {lista_consolas}")
print(f"Indexado juegos: {lista_juegos[0:2]}")
print(f"Número de elementos consolas: {len(lista_consolas)}")
print(f"Concatenación: {lista_consolas + lista_juegos}")
print("-------- FIN LISTAS --------")
#Inputs
#print("Texto introducido:" + input("Introduce texto: "))
