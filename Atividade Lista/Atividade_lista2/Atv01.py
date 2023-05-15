meses= ["1- janeiro", "2- Fevereiro", "3-Março", "4-Abril", "5-Maio", "6-Junho", "7-Julho", "8-Agosto", "9-Setembro", "10-Outubro", "11-Novembro", "12-Dezembro"]
tempe=[]

for cont in range(1,6):
    tempe.append(int(input("Digite a temperatura: ")))

print("-"*30)
soma_ano=sum(tempe)
media_ano=int(soma_ano/5)
print(f"A temperatura média anual é {media_ano}")

for cont2 in range(1,6):
    print(tempe)
    if (tempe >= media_ano):
        print("Janeiro")
    elif (tempe >= media_ano):
        print("Fevereiro")
    elif (tempe >= media_ano):
        print("Março")
    elif (tempe >= media_ano):
        print("Abril")
    elif (tempe >= media_ano):
        print("Maio")
    elif (tempe >= media_ano):
        print("Junho")
    elif (tempe >= media_ano):
        print("Julho")
    elif (tempe >= media_ano):
        print("Agosto")
    elif (tempe >= media_ano):
        print("Setembro")
    elif (tempe >= media_ano):
        print("Outubro")
    elif (tempe >= media_ano):
        print("Novembro")
    elif (tempe >= media_ano):
        print("Dezembro")