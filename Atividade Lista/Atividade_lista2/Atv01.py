meses= ["1- janeiro", "2- Fevereiro", "3-Março", "4-Abril", "5-Maio", "6-Junho", "7-Julho", "8-Agosto", "9-Setembro", "10-Outubro", "11-Novembro", "12-Dezembro"]
tempe= []

for perc in meses:
    temperatura=(int(input(f"Digite a temperatura para o mês {perc}: ")))
    tempe.append(temperatura)
    
print(tempe)
print("-"*30)
soma_ano=sum(tempe)
media_ano=int(soma_ano/12)
print(f"A temperatura média anual é {media_ano}")
i=1
for i, temperatura in enumerate(tempe, start=1):
        if temperatura > media_ano:
            print(f"A temperatura {temperatura} do mês {meses[i]} é maior que a média anual {media_ano}")
            