#1. Cuántos (*) enviará el siguiente fragmento de código a la consola:
print("###############################")
print("######## Ejercicio 1 ##########")
print("###############################")
i=1
while (i<=3):
    i+=2
    print("*")

#2. Cuántos (*) enviará el siguiente fragmento de código a la consola:
print("###############################")
print("######## Ejercicio 2 ##########")
print("###############################")
i=1
while (i<=5):
    i+=1
    if (i%2 ==0):
        print("*")
    break

#3. Cuántos (#) enviará el siguiente fragmento de código a la consola:
print("###############################")
print("######## Ejercicio 3 ##########")
print("###############################")

for i in range (1):
   print("#")
else:
   print("#")

#4. Crea un bucle for con una sentencia break. El programa deberá iterar sobre los caracteres en una dirección de 
# correo electrónico y salirse del bucle cuando llegue al signo @ e imprimir la parte antes del @ en una línea 
print("###############################")
print("######## Ejercicio 4 ##########")
print("###############################")

direccion_correo = "usuario@dominio.com"

# Iteramos sobre los caracteres en la dirección de correo
for caracter in direccion_correo:
    if caracter == "@":
        break  # Salir del bucle cuando se encuentre el "@".
    print(caracter, end="")

# Imprimir la parte antes del "@"
print("\n")

#5. Crear un bucle for que cuente del 0 al 10 e imprima números impares en la pantalla
print("###############################")
print("######## Ejercicio 5 ##########")
print("###############################")

for numero in range(11):  # Iterar del 0 al 10
    if numero % 2 != 0:  # Comprobar si el número es impar
        print(numero)
