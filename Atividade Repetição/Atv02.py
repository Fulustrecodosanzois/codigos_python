valor= 50
total = 0
acum = 0

for cont in range (2):
    nome= input("Digite seu nome: ")
    diaria= int(input("Quantas diárias utilizou: "))
    if diaria < 15:
        soma = diaria * 4
        soma2 = (valor * diaria) + soma
        print(F"{nome}, o valor total de suas diárias é: {soma2}")
    elif diaria == 15:
        soma = diaria * 3,60
        soma2 = (valor * diaria) + soma
        print(F"{nome}, o valor total de suas diárias é: {soma2}")
    elif diaria > 15:
        soma = diaria * 3
        soma2 = (valor * diaria) + soma
        print(F"{nome}, o valor total de suas diárias é: {soma2}")
        
acum= soma2

print(f"O total de lucro do hotel {acum}")