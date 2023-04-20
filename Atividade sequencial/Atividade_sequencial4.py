lata = int(input("Qual a quantidade de latas de 350ml? ", ))
garrafa600 = int(input("Qual a quantidade de garrafas de 600ml? "))
garrafa2l = int(input("Qual a quantidade de garrafas de 2 litros? "))

comprou = (lata*350 + garrafa600*600 + garrafa2l*2000) /1000

total = (comprou/1000)

print("O comerciante comprou ", comprou, "litros")

