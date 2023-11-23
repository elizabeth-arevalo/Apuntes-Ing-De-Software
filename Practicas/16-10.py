### Diseña un programa que utilice un ciclo while y que le pida continuamente al usuario que ingrese una palabra, 
# a menos que ingreses "termina" como la palabra de salida secreta; en cuyo caso imprimirá el caso 
# "Haz dejado el bucle con éxito" y el bucle terminará. 
# Utiliza el concepto de ejecución condicional y utiliza break

print("###############################")
print("######## Ejercicio 1 ##########")
print("###############################")
print("Ingresa una palabra")
palabra = (str(input("")))

while palabra != "termina":
    if palabra != "termina":
        print("Ingresa una palabra")
        palabra = (str(input("Palabra: ")))
        continue
    else:
        print("Haz dejado el bucle con éxito")
        break

## Escribe un programa que use un bucle FOR auxiliado de un instrucción condicional y la sentencia Continue. 
# El programa deberá pedir al usuario que ingrese una palabra , deberá borrar las vocales de la misma palabra. 
# Imprimir las letras no borradas en una línea separada.

print("###############################")
print("######## Ejercicio 2 ##########")
print("###############################")
# Pedir al usuario que ingrese una palabra
palabra2 = input("Ingrese una palabra: ")

# Crear una variable para almacenar las letras no borradas
letras_no_borradas = ""

# Iterar a través de cada letra en la palabra
for letra in palabra2:
    # Verificar si la letra es una vocal (mayúscula o minúscula)
    if letra.lower() in "aeiou":
        continue  # Saltar a la siguiente iteración del bucle si es una vocal
    letras_no_borradas += letra  # Agregar la letra a las letras no borradas

# Imprimir las letras no borradas
print("Letras no borradas:", letras_no_borradas)

# Crear un bucle for que cuente un número del 0 al 10 e imprima únicamente los números impares.

print("###############################")
print("######## Ejercicio 3 ##########")
print("###############################")

numero=0
for numero in range(10):
    if numero % 2==0:
        continue
    print(numero)
    numero+=numero
    

    
# Crear un bucle while que cuente un número del 0 al 10 e imprima únicamente los números impares.

print("###############################")
print("######## Ejercicio 4 ##########")
print("###############################")

var=0
while var<10:
    var +=1
    if var % 2 ==0:
        continue
    print(var)

# Crear un programa con un bucle for y una sentencia continue, el programa deberá iterar sobre una cadena de 
# digitos, reemplazar cada 0 por una X e imprimir la cadena modificada en la pantalla

print("###############################")
print("######## Ejercicio 5 ##########")
print("###############################")
cadena= input("Ingresa la cadena de números con 0: ")
for ceros in cadena:
    if ceros in "0":
        cadena=cadena.replace("0", "X")
print(cadena)