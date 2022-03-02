# Portafolio-de-fundamentos-de-programaci-n
# Qué es Python?
Python es un lenguaje de programación interpretado,sencillo de leer y escribir debido a su alta similitud con el lenguaje humano. Además, se trata de un lenguaje multiplataforma de código abierto y, por lo tanto, gratuito, lo que permite desarrollar software sin límites

# Qué es una variable?
Una variable se declara para indicarle al programa a partir de qué lugar empieza a existir, qué nombre tendrá y qué tipo de datos almacenará,es un elemento que se emplea para almacenar y hacer referencia a otro valor o para explicarlo de una manera mas sencilla es una caja que guarda zapatos, la caja es la varuable y los zapatos el valor a asginar.

## Nombrando una variable
La creación de variables se realiza a través de la asignación de un valor a la misma.
El operador de asignación en Python es el “=“
'''x = 100                                                      100=x'''
De derecha a izquierda                                       De izquierda a derecha
"correcto"                                                   "incorrecto"
## Asignando valores a una variable
Asignación en la misma línea:
x = 5; y = 9; z = 12
• Asignación múltiple:
day, month, year = “miércoles”
,
”mayo”
, 2016
• Asignación del mismo valor:
largo = ancho = 4
• Asignación de intercambio:
base = 15; altura = 30
base, altura = altura, base


## Operadores básicos
+ suma
- resta
* multiplicacion
* division
* division euclidiana (cociente)
* módulo
* potencia

### Suma
```python
 num1=6
 num2=10
 sum1=num1+num2
 print(sum1)
```
### Resta
```python
num1=10
num2=7
resta=num1-num2
print(num1,'-',num2,'=',resta)
```

### Multiplicación
```python
* num1=10
* num2=7
- mult=num
* print(num1,'*',num2,'=',mult)
```

### División
```python
* num1=10
* num2=7
* divi=num1/num2
* print(num1,'/',num2,'=',divi)
```

### Módulo
```python
* num1=10
* num2=7
* modulo=num1%num2
* print(num1,'%',num2,'=',modulo)
```

# Tipos de datos en Python
Los tipos de datos serían:
* Numeros enteros
* Numeros de punto flotante
*  Texto (cadenas de caracteres)
*  Booleanos (Verdadero y falso)

## Casting en Python
 El casting es la tecnica que sirve para convertir un dato de un tipo a un tipo de dato diferente
 ```python
   int a str: str(45)
   str a int: int ("123")
   float a int: int (3.5)
```

## Integer
```python
dia="lunes"
print(type(dia))
```

## Float
```python
dia=21
print(type(dia))
```

## String
```python
dia=21.5
print(type(dia))
```

## List
Una lista es una estructura de datos en Python que es una secuencia de elementos ordenados mutables o cambiables. Cada elemento o valor que está dentro de una lista se denomina elemento. Así como las cadenas se definen como caracteres entre comillas, las listas se definen con valores entre corchetes [ ]
```python
list_1 = [ 1,6,9]
print(list_1)

list_2 = [ 5,6]
print(list_2)
```

## Tuple
Una tupla es una colección de objetos de Python separados por comas. De alguna manera, una tupla es similar a una lista en términos de indexación, objetos anidados y repetición, pero una tupla es inmutable a diferencia de las listas que son mutables.
```python
()
(1,2,4,5,6,7,8,9)
("Hola", "me", "llamo","Brando")

```

## Dictionary

# Tomando decisiones

## Sentencia if

## Ciclo For

## Ciclo While

## Break

## Continue
