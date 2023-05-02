codigo = int(input("Digite o código do funcionário: "))
nasc = int(input("Digite o ano de nascimento: "))
ingresso = int(input("Digite o ano de contratação: "))

idade = 2023 - nasc

tempo_trabalho = 2023 - ingresso

if idade >= 65:
    print(f"Sua idade é {idade}, com o tempo de trabalho de {tempo_trabalho}. Requerer aposentadoria!!!")
elif tempo_trabalho > 30:
    print(f"Sua idade é {idade}, com o tempo de trabalho de {tempo_trabalho}. Requerer aposentadoria!!!")
elif idade >= 60 and tempo_trabalho >= 25:
    print(f"Sua idade é {idade}, com o tempo de trabalho de {tempo_trabalho}. Requerer aposentadoria!!!")
else:
    print(f"Sua idade é {idade}, com o tempo de trabalho de {tempo_trabalho}. Não requerer aposentadoria!!!")
