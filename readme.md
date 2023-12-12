# Guía python

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

### Index - String - *PENDIENTE*
Función: index(valor, inicio, fin)

**Ejemplos:**
```python
parrafo = """Utilizamos el método index( ) para explorar strings, ya que
permite hallar el índice de aparición de un caracter o cadena de
caracteres dentro de un texto dado."""
print(parrafo.index("explorar"))
print(parrafo.rindex("explorar"))
print(parrafo[2])
```

### Substrings - *PENDIENTE*

```python

```

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
- Crear carpeta/carpetas: `os.makedirs(ruta)`


#### Path - *Importado*
Se importa -> **from** pathlib **import** Path
La clase path permite leer estructuras de carpetas y archivos.


- Directorio raiz: `Path.home()`
- Ruta relativa: `Path("Carpeta_1", "Carpeta_2", "archivo.md")`
- Ruta absoluta: `Path(Path.home(), "Carpeta_1", "Carpeta_2", "archivo.md")`

```python

```


### Ejemplo

```python

```
