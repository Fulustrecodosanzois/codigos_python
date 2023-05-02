litros_vendidos = int(input("Quantos litros foram vendidos? "))
tipo_combustivel = input("Qual o tipo de combustível: \n *g* para Gasolina \n *a* para Álcool\n")

gasolina = 4.80
alcool = 3.10

if tipo_combustivel == "a":
    soma = alcool*litros_vendidos
    if litros_vendidos <= 20:
        soma = alcool - (3/100*alcool)
        print(soma)
    
print(soma)