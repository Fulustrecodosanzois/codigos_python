while True: # enquanto A for diferente de B o loop continua
    a= int(input("Digite um valor: "))
    b= int(input("Digite outro valor: "))
    if a != b:
        break
        
def Soma_impar (inicial, final):
    soma = 0
    for cont in range (inicial, final+1):
        if cont % 2 == 1:
            soma+= cont
    return soma

def media_multiplo3(inicial, final):
    total= 0
    contDivisores = 0
    for cont in range (inicial, final+1):
        if cont % 3 == 0:
            total+= cont #isto é para somar todos os divisores
            contDivisores += 1 # isto é para contar todos os divisores
            
    return total / contDivisores

if a < b:
    print(f"A soma dos valores é: {Soma_impar(a,b)}")
    
else:
    print(media_multiplo3(b,a))