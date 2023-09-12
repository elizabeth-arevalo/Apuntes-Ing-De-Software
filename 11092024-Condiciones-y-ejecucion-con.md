# Condiciones y ejecución condicional.

### Introducción

Debe existir un mecanismo en Python que le permita hacer algo si se cumple una condición y no funciona si no se cumple. Es como la vida real haces ciertas cosas o no cuando se cumple una condición específica.

Por ejemplo:
- Sales a caminar si el clima es adecuado o te quedas en casa si está haciendo frío.

## Desarrollo 

Para tomar tales decisiones Python ofrece una instrucción especial que se denomina intrucción condicional.

Existen distintas variables de la misma, empezando con la más simple:

### Sentencia If.

1. Sintaxis if. 
    ~~~
    if true or not:
        do this if true
    ~~~
    
    - Ejemplo:

    ~~~
    if (edad => 18):
        print("La persona es mayor de edad")
    ~~~

### Sentencia If ... else.
Ahora sabemos lo que hacemos si se cumplen las condiciones, es como hacer un plan B.

Python nos permite empezar dichos planes alternativos, esto se hace con una segunda forma ligeramente más compleja de la sentencia condicional. La sentencia **If ... else**

2. Sintaxis If ... else
    ~~~
    if true or false:
        do this if true
    else
        do this if false
    ~~~