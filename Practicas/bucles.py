print("Programa para calcular el impuesto a pagar")
ingreso = float(input("Ingresa tu salario: "))
if (ingreso <= 85528) :
    impuesto = ingreso * 0.18
    print("El impuesto que debes pagar es: ", impuesto)
elif (ingreso < 85528) :
    impuesto = ingreso * 0.36
    print("El impuesto que debes pagar es: ", impuesto)
else:
    print("El impuesto a pagar es: ", 0)