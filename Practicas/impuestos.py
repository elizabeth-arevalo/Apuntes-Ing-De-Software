print("calculo de impuestos")
salario = int(input("Ingresa tu salario: "))

# a) Si el ingreso no era superior a $85528 pesos el impuesto era igual al 18%
# b) Si el ingreso era superior a esta cantidad el impuesto se duplicaba. 
if salario <= 85528 and salario > 0 :
    impuesto=salario*0.18
elif  salario > 85528 :
    impuesto=salario*0.36
else:
    impuesto=0
    
print("El impuesto calculado es: ", impuesto)
