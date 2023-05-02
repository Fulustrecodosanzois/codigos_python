hora_extra = 0
valor_hora = int(input("Qual valor da hora de trabalho? "))
soma = []

#salário hora médio 16,00

for cont in range(4):
    horas = int(input("Digite as horas trabalhadas:"))
    if horas > 40:
        hora_extra = valor_hora * 1.5
        horas *= valor_hora + hora_extra  
        soma= horas
        
        
print(f"Seu salário é {soma}")