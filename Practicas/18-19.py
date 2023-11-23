# Programa en Python. 
# Tipos de billetes: 100,50,20. 
# 1. Solicitar al usuario la cantidad de dolares. 
# 2. Vamos a hacer la conversión a peso mexicano. 
# 3. Vamos a entregar el cambio en estos 3 billetes
# 1 dolar = 17 pesos mexicamos
# ¿Cuantos billetes de cada denominación entrego.
# $100 = 17*100 = 1700. 
# De 100 - 15 billetes
# De 50 - 2 billetes
# De 20 - 5 billetes


# Solicitar al usuario la cantidad de dólares
dollars = float(input("Ingrese la cantidad de dólares: "))

# Realizar la conversión a pesos mexicanos
pesos = dollars * 17
print("La conversión a pesos da: ", pesos)
# Calcular la cantidad de billetes de cada denominación
billetes_100 = int(pesos / 100)
billetes_50 = int((pesos % 100) / 50)
billetes_20 = int(((pesos % 100) % 50) / 20)

# Imprimir la cantidad de billetes de cada denominación a entregar
print(f"Se deben entregar:\n"
      f"Billetes de $100: {billetes_100}\n"
      f"Billetes de $50: {billetes_50}\n"
      f"Billetes de $20: {billetes_20}")


