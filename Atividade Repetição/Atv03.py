masc= ("1")
fem= ("2")
maior= 0
media= 0

for cont in range(1):
    altura= float(input("Qual sua altura? "))
    sexo= str(input("Qual seu sexo? "))
    if altura > maior:
        maior= altura
    if cont == 1:
        menor= altura
    elif altura >= maior:   
        maior= altura
    elif altura <= menor:
        menor= altura
    elif sexo == "2":
        media= altura
        print(altura)
        
#print(F"A maior altura é {maior}")            
        