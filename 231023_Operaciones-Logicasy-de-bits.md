# Operaciones lógicas y de bits en Python.

### Introducción.

En esta sección aprenderás sobre los operadores lógicos, así como de bit a bit en Python, además de los conceptos de las tablas de verdad y el desplazamiento de bits.

### Lógica de computadoras.

Python cuenta con operadores para construir con funciones y disyunciones.

#### Conjuncion lógica

Un operador de **conjuncion lógica** en Python es la palabra AND. Es un operador binario con una prioridad inferior a la expresada por los operadores de comparación. Nos permite codificar condiciones complejas sin el uso de parentesis.

Ejemplo: 

~~~
counter > 0 and value == 100
~~~

El resultado propocionado por el valor **and** se puede determinar sobre la base de la tabla de verdad.

Tabla de verdad:

| A | B | AND |
|----------|---------|---------|
| False    | False   | False   |
| False    | True    | False   |
| True     | False   | False   |
| True     | True    | True    |

#### Disyunción lógica

Un operador de **disyunción lógica** en Python es la palabra OR. Es un operador binario con una prioridad más baja que **and** al igual que pasa con la suma o una multiplicación (+/or < */and) a la expresada por los operadores de comparación. Nos permite codificar condiciones complejas sin el uso de paréntesis.

| A | B | OR |
|----------|---------|---------|
| False    | False   | False   |
| False    | True    | True    |
| True     | False   | True    |
| True     | True    | True    |

#### Negación lógica

Además hay otro operador que se puede aplicar par condiciones de construcción. Es un operador unario que realiza una negación lógica. Su funcionmiento es simple, convierte la verdad en falso y lo falso en verdad

| A | NOT |
|----------|---------|
| True     | False   | 
| False    | True    | 

Este operador se escribe con la palabra **not** y su prioridad es muy alta.


### Expresiones lógicas.

Una expresión es una combinación de operadores y operandos que se interpreta para producir algún otro valor.

Ejemplo:

~~~
var=3
print( var > 0 )
print(not( var <= 0 ))
print( var != 0)
print(not(var==0))
~~~

### Valores lógicos contra bits individuales.

Los operadores lógicos, toman sus argumentos como un todo, independientemente de cuantos bits contengan. Los operadores solo conocen el valor 0 y 1.

~~~
i=1
j=not(not(i))

print(i, j)
~~~

Sin embargo hay 4 operadores que le permiten manipular operadores denominados bit a bit. 

Cubren todas las operaciones que mencionamos anteriormente, en el contexto lógico y un operador adicional, este es el operador **XOR**. Significa OR exclusivo y se denota como ^
Se conoce como acento circunflejo o signo de intercalación.


| A   | B   | A&B | A/B | A^B |
|-----|-----|-----|-----|-----|
| 0   | 0   | 0   | 0   | 0   |
| 1   | 0   | 0   | 1   | 1   |
| 0   | 1   | 0   | 1   | 1   |
| 1   | 1   | 1   | 1   | 0   |

| A |  ~A |
|---|-----|
| 1 | 0   | 
| 0 | 1   | 

Los argumentos de estos solo deben ser enteros