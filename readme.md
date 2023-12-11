# Guía python

## ????

- Importar función: **from** modulo **import** funcion
- Definir función: **def** nombre_funcion():

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

### Index - String ??????
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

### Substrings - ????

```python

```







### Path - *Importado*
La clase path permite leer estructuras de carpetas y archivos.
Se importa -> **from** pathlib **import** Path

- Directorio raiz: `Path.home()`
- Ruta relativa: `Path("Carpeta_1", "Carpeta_2", "archivo.md")`
- Ruta absoluta: `Path(Path.home(), "Carpeta_1", "Carpeta_2", "archivo.md")`

```python

```


### Ejemplo

```python

```