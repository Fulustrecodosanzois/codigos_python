maior= 0
media_turma= 0
media_mulheres = 0
soma_turma= 0
soma_mulheres= 0
cont_mulheres= 0


for cont in range(1,4):
    altura= float(input("Qual sua altura? "))
    sexo= str(input("Qual seu sexo? "))
    if altura >= maior:
        maior= altura
    if cont == 1:
        menor= altura
    elif altura >= maior:   
        maior= altura
    elif altura <= menor:
        menor= altura
    elif sexo == 2:
        soma_mulheres += altura
        cont_mulheres += 1
        
    soma_turma+= altura


print("-" * 20)        
print(F"A maior altura é {maior}\n")            
print(F"A menor altura é {menor}\n")   
print(f"A média de alturas da turma é {soma_turma / 6}\n")
print("-" * 20) 
        