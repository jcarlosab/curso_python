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
print(f"100/3 = {100/3} redondeo [round()] {round(100/3)}")
print(f"100/3 = {12/7,2} redondeo [round()] {round(12/7,2)}")
print(f"100/3 = {100/3} redondeo [round(num, ndigits)] {round(100/3, 3)}")

#Index - index(value, start, end)
parrafo = """Utilizamos el método index( ) para explorar strings, ya que
permite hallar el índice de aparición de un caracter o cadena de
caracteres dentro de un texto dado."""
print(parrafo.index("explorar"))
print(parrafo.rindex("explorar"))
print(parrafo[2])

#Substrings

#Inputs
#print("Texto introducido:" + input("Introduce texto: "))
