dig = []

for cont in range(5):
    num = int(input("Digite um número: "))
    dig+= [num]
    
maior= max(dig)

print(f"Os números digitados foram {dig}\n")
print(F"O maior número digitado foi {maior}")


#-----------------------------------------------------

valor = int(input("Informe um valor qualquer: "))

maior= 0
posicao= 0 

for contador in range (1, valor + 1):
    item = int(input("Informe um valor: "))
    maior= item
    posicao = contador
    
print("o valor maior é {maior} e está na posição {posicao}") 



