## Determina el número más grande ingresado
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

if number1 > number2:
    larger_number= number1
else:
    larger_number= number2
    
print("El número mayor es: ", larger_number)

###########################################
####### Elige el número más grande ########
###########################################

if number1 > number2: larger_number= number1
else: larger_number= number2

### Imprime el resultado
print("El número mayor es: ", larger_number)

##############################################
# Escribir un programa el mayor de 3 números #
##############################################

n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

if n1 > n2 and n1 > n3:
    max=n1
elif n2 > n1 and n2 > n3:
    max=n2
else:
    max=n3
    
print("El número mayor es: ", max)

    




