print("Convirtamos pesos colombianos a dólares")
pesos = int(input("¿Cuánto dinero tienes? $"))

dolar = 4811.09
dolarApesos = pesos/dolar
dolarApesos = round(dolarApesos,2)

print(f"Usted tiene USD ${dolarApesos}")