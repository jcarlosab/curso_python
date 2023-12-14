# Guía python

- [Guía python](#guía-python)
  - [Importar y definir funciones en python](#importar-y-definir-funciones-en-python)
  - [Operadores](#operadores)
  - [Tipos de datos](#tipos-de-datos)
    - [Strings](#strings)
      - [Metodos string *Pendiente*](#metodos-string-pendiente)
  - [Funciones](#funciones)
    - [Print](#print)
    - [Input](#input)
    - [Round - Importada](#round---importada)
    - [Index](#index)
    - [Substrings](#substrings)
    - [Strings - *Pendiente*](#strings---pendiente)
      - [Análisis](#análisis)
      - [Transformación](#transformación)
      - [Separación y unión](#separación-y-unión)
    - [Propiedades strings](#propiedades-strings)
    - [Listas](#listas)
    - [Diccionarios](#diccionarios)
    - [Tuples](#tuples)
    - [Sets](#sets)
    - [if](#if)
    - [for](#for)
    - [while](#while)
    - [range](#range)
    - [enumerate](#enumerate)
    - [zip](#zip)
    - [min y max](#min-y-max)
    - [random](#random)
    - [Compresión de listas](#compresión-de-listas)
    - [Funciones](#funciones-1)
      - [return](#return)
      - [Parámetro \*args](#parámetro-args)
      - [Parámetro \*\*kwargs](#parámetro-kwargs)
    - [Open, Read y Write](#open-read-y-write)
    - [Directorios](#directorios)
      - [Os - *Importado*](#os---importado)
      - [Path - *Importado*](#path---importado)


## Importar y definir funciones en python

- Importar función: `from modulo import funcion`
- Definir y llamar funciones: 
```python
def nombre_funcion(): #Declaración de función
    print("Mi nueva función")

nombre_funcion() #Llamada a funcion
```

## Operadores

| Operador       | Símbolo |
| :------------- | :-----: |
| Suma           |    +    |
| Resta          |    -    |
| Multiplicación |   \*    |
| División       |    /    |
| Cociente       |   //    |
| Resto          |    %    |
| Potencia       |  \*\*   |
| Raíz cuadrada  | \*\*0.5 |

| Operadores lógicos | Símbolo |
| :----------------- | :-----: |
| Igual              |   ==    |
| Diferente          |   !=    |
| Mayor              |    >    |
| Menor              |    <    |
| Mayor igual        |   >=    |
| Menor igual        |   <=    |
| y                  |   and   |
| o                  |   or    |
| no                 |   not   |

## Tipos de datos

| Tipo de dato |      Operación       |
| :----------- | :------------------: |
| int          |      numero = 1      |
| float        |     numero = 1.2     |
| string       | texto = "Hola mundo" |
| boolean      |  valor= true/false   |

### Strings

La \ indica que debe ser tratado como un caracter especial.

| Carac. especiales | Operación |
| :---------------- | :-------: |
| Comillas          |    \"     |
| Salto de línea    |    \n     |
| Tabular           |    \t     |
| Barra             |    \\     |

**Notas:**

```python
texto = "Se pueden " + "concatenar"
```

**Notas:**

```python
type(variable) #Nos indica de que tipo es una variable.
float(variable) #Convierte un entero a decimal
int(variable) #Convierte un decimal a entero
```
#### Metodos string *Pendiente*
Analisis
Transformación
Separación y unión

## Funciones

### Print

```python
print("Hola mundo") #Pintar una línea de texto
print("""
Bloque
de
texto
""")
print("Hola" + " " + "mundo") #Concatenar cadenas de texto
print("Comillas: \" " + "Barra: \\ " + " \t Tabulador" + "\n Salto linea " )
print(100 + 120) #Pintar operaciones con print
```
Se pueden pintar variables dentro del print formateando la cádena usando print(f"{}") o print("texto {}".format(valor))

**Ejemplos:**
```python
#Formateo antiguo
print("Valor actual {} nuevo valor {}".format(valor_actual, valor_nuevo))
#Formateo actual
print(f"Permite pintar variables usando {variable}")
```

### Input

Muestra el texto y permite almacenar lo escrito

```python
input("Introduce texto: ")
```
### Round - Importada
Función: round(valor, numero_digitos)
- valor -> indicamos la cifra a redondear.
- numero_digitos -> (Opcional) indicamos el número de digitos a redondear.

**Ejemplos:**
```python
numero = round(100/3)
numero_dos_dig = round(100/3, 2)
numero_tres_dig = round(100/3, 3)
```

### Index
Función: index(valor, inicio, fin)

**Ejemplos:**
```python
parrafo = """Utilizamos el método index( ) para explorar strings, ya que permite hallar el índice de aparición de un caracter o cadena de caracteres dentro de un texto dado."""
print(parrafo.index("explorar"))
print(parrafo.rindex("explorar"))
print(parrafo[2])
```

### Substrings
Selecciona los caracterés del texto comprendido entre dos indices

**Ejemplo:**
```python
mi_texto = "Hola_mundo"
mi_texto[0:4] #Muestra el texto de la posición dada "Hola"
mi_texto[2::3] #Muestra el texto de la posición dada "lmd"
mi_texto[::-1] #Muestra el texto al revés "odnum_aloH"
```
### Strings - *Pendiente*

#### Análisis
- Método count() | Test cuenta repeticiones de 'Hola' en 'Hola mundo': 1
- Método find() | Test buscar 'Hola' en 'Hola mundo': 0
- Método find() | Test buscar '123' en 'Hola mundo': -1
- Método rfind() | Test buscar desde el final 'Hola' en 'Hola mundo': 0
- Método index() | Test buscar 'Hola' en 'Hola mundo': 0
- Método rindex() | Test buscar desde el final 'Hola' en 'Hola mundo': 0
- Método startswith() | Test 'Hola mundo' empieza con 'Hola': True
- Método endswith() | Test 'Hola mundo' acaba con 'Hola': False
- Método isdigit() | Test dígitos '123456': True
- Método isnumeric() | Test números '123456': True
- Método isdecimal() | Test decimales '123456': True
- Método isalnum() | Test alfanuméricos '123456': True
- Método isalpha() | Test alfabéticos 'abcdefg': True
- Método islower() | Test todo minúsculas 'abcdefg': True
- Método isupper() | Test todo mayúsculas 'abcdefg': False
- Método isprintable() | Test imprimibles 'abcdefg' (no son caracteres especiales): True
- Método isspace() | Test espacios '   ' solo espacios: True

#### Transformación
- Método capitalize() | Test primera letra en mayúscula 'abcdefg': Abcdefg
- Método encode() | Test codifica la cadena con el mapa de caracteres especificado y retorna una instancia del tipo byte 'abcdefg': b'abcdefg'
- Método replace() | Test reemplazar 'mundo' por 'mundo2' en 'Hola mundo': Hola mundo2
- Método lower() | Test todo a minúsculas 'ABC': abc
- Método upper() | Test todo a mayúsculas 'abc': ABC
- Método swapcase() | Test cambia minúsculas por mayúsculas 'Ja Ja Ja Ja Ja': jA jA jA jA jA
- Método strip() | Test quita espacios en blanco izquierda y derecha en '  Hola   ': Hola FIN
- Método lstrip() | Test quita espacios en blanco izquierda  en '  Hola   ': Hola    FIN
- Método rstrip() | Test quita espacios en blanco derecha  en '  Hola   ':   Hola FIN
- Método center() | Test alinear al centro 'abc':         abc         
- Método ljust() | Test alinear a la izquierda 'abc': abc                 
- Método rjust() | Test alinear a la derecha 'abc':                  abc

#### Separación y unión
- Método split() | Test separar cadena por defecto ('1 2 3 4 5 6'.split()) '1 2 3 4 5 6': ['1', '2', '3', '4', '5', '6']
- Método split() | Test separar cadena por guiones ('1-2-3'.split('-')) '1-2-3': ['1', '2', '3']
- Método splitlines() | Test dividir con salto de linea 'Hola \n mundo': ['Hola ', ' mundo']
- Método partition() | Test partition parte texto en tres partes ('Prueba ', 'texto', ' para funcion')
- Método rpartition() | Test rpartition parte texto en tres partes ('Prueba ', 'texto', ' para funcion')
- Método join() | Test join tuple sin separador ps1ps2ps3
- Método join() | Test join tuple con separador '#' ps1#ps2#ps3
- Método join() | Test join diccionario con separador '#' nombre#apellidos

### Propiedades strings
*Pendiente*
### Listas
*Pendiente*
### Diccionarios
*Pendiente*
### Tuples
*Pendiente*
### Sets
*Pendiente*

### if
*Pendiente*
### for
*Pendiente*
### while
*Pendiente*
### range
*Pendiente*
### enumerate
*Pendiente*
### zip
*Pendiente*
### min y max
*Pendiente*
### random
*Pendiente*
### Compresión de listas
*Pendiente*
### Funciones
*Pendiente* 
#### return
*Pendiente*
#### Parámetro *args
*Pendiente*
#### Parámetro **kwargs
*Pendiente*

### Open, Read y Write
- Abrir un archivo: `open('archivo', 'modo')`
  - archivo -> documento a abrir
  - modo -> Parametros de apertura (r, a, w, x):
    - **Read**(Lectura): `open('archivo.txt', 'r')`
    - **Append**(Añadir): `open('archivo.txt', 'a')`
    - **Write**(Escritura): `open('archivo.txt', 'w')`
    - **Create**(Crear): `open('archivo.txt', 'x')`
La función `open()` devuelve un objeto de tipo archivo al que se le pueden aplicar los metodos:
- Leer un archivo de texto: `obj_archivo.read()`
- Pintar una linea del archivo: `obj_archivo.readline()`
- Devolver una lista con las lineas: `obj_archivo.readlines()` (Usar solo con archivos pequeños)
  
**Ejemplos read:**
```python
archivo = open('text.txt')
print(archivo.read()) #Pinta el contenido del fichero
print(archivo.readline()) #Pinta una linea del archivo por cada ejecución del readline
print(archivo.readline().rstrip()) #rstrip evita el salto de linea en los archivos
print(archivo.readline().upper()) #upper pinta la linea en mayúsculas 
print(archivo.readlines()) #Devuelve una lista 
archivo.close()
```
- Escribir en el archivo: `obj_archivo.write('Texto')`

**Ejemplos write:**
```python
archivo = open('text.txt', 'w') #Con w sustituye todo el archivo
#archivo = open('text.txt', 'a') #Con a añade al final del archivo
archivo.write("Nuevo texto") #Pinta en una línea
archivo.write('''Texto en
varias
líneas''')
archivo.close()
```                    
- Cerrar archivo abierto: `obj_archivo.close()`

**Nota:** El objeto obj_archivo una vez abierto se puede iterar con un bucle for: `for linea in obj_archivo:`

### Directorios

#### Os - *Importado*
Se importa -> **import** os
Lo usamos para trabajar con archivos que están en dirtectorios diferentes a nuestro código.

- Obtener directorio actual: `os.getcwd()`
- Cambiar de directorio: `os.chdir(ruta)`

**Ejemplo:**
```python
import os

#Abrir archivo.txt en ruta C:\Users\Carpeta\archivo.txt
os.chdir('C:\\Users\\Carpeta') #Ejemplo ruta windows
archivo = open('archivo.txt') #Abre el archivo dentro del nuevo directorio
archivo.read() #Leemos el archivo

#Recuperar la siguiente ruta: C:\Users\Carpeta\archivo.txt
ruta = 'C:\\Users\\Carpeta\\archivo.txt'
os.path.basename(ruta) #Obtiene el valor archivo.txt
os.path.dirname(ruta) #Obtiene la ruta C:\\Users\\Carpeta
os.path.split(ruta) #Devuelve la ruta C:\\Users\\Carpeta y el nombre de base
``` 
- Borrar directorio: `os.rmdir(ruta)` (Indicar ruta completa de carpeta a borrar)
- Crear carpeta/carpetas: `os.makedirs(ruta)`

#### Path - *Importado*
Se importa -> **from** pathlib **import** Path
La clase path permite leer estructuras de carpetas y archivos.

- Directorio raiz: `Path.home()`
- Ruta relativa: `Path("Carpeta_1", "Carpeta_2", "archivo.md")`
- Ruta absoluta: `Path(Path.home(), "Carpeta_1", "Carpeta_2", "archivo.md")`
- Devolver un nuevo objeto path cambiando el nombre de archivo: `Path.home().with_name('prueba.txt')`
```python
from pathlib import Path

base = Path.home()
ruta = Path("Carpeta", "mi_texto.txt") #Ruta completa con mi_texto.txt
ruta2 = ruta.with_name('prueba.txt') #Ruta completa con prueba.txt
```
- Devolver padre inmediato de una ruta de archivos: `ruta.parent` se pueden ir añadiendo más .parent para ir subiendo de carpeta.
- Buscar dentro de una ruta:
```python
from pathlib import Path

base = Path.home()
#Busca en la carpeta base archivos txt
for archivo in Path(base).glob("*.txt"):
  print(archivo)
#Busca en todas las carpetas y subcarpetas los archivos txt
for archivo in Path(base).glob("**/*.txt"): 
  print(archivo)
```
